/*
    Stripe Payment Processing
    Based on Stripe's official documentation:
    https://stripe.com/docs/payments/accept-a-payment
*/

document.addEventListener("DOMContentLoaded", function () {
    // Get Stripe public key and client secret from the template
    var stripePublicKey = document.getElementById("id_stripe_public_key").textContent.trim();
    var clientSecret = document.getElementById("id_client_secret").textContent.trim();

    // Initialize Stripe.js
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    // Define styling for the Stripe card input
    var style = {
        base: {
            color: "#000",
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": { color: "#aab7c4" },
        },
        invalid: {
            color: "#dc3545",
            iconColor: "#dc3545",
        },
    };

    // Create and mount Stripe card element
    var card = elements.create("card", { style: style });
    card.mount("#card-element");

    // Handle real-time validation errors on the card element
    card.on("change", function (event) {
        var errorDiv = document.getElementById("card-errors");
        errorDiv.textContent = event.error ? event.error.message : "";
    });

    // Handle form submission
    var form = document.getElementById("payment-form");
    var submitButton = document.getElementById("submit-button");
    var processing = false; // Prevent multiple submissions

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        if (processing) return;
        processing = true;

        // Disable card and button during processing
        card.update({ disabled: true });
        submitButton.disabled = true;
        submitButton.textContent = "Processing...";

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name ? form.full_name.value : "",
                    email: form.email ? form.email.value : "",
                    phone: form.phone_number ? form.phone_number.value : "",
                },
            },
        }).then(function (result) {
            if (result.error) {
                // Display error message
                var errorDiv = document.getElementById("card-errors");
                errorDiv.textContent = result.error.message;
                submitButton.disabled = false;
                submitButton.textContent = "Pay Now";
                processing = false;
                card.update({ disabled: false });
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    window.location.href = form.action; // Redirect to success page
                }
            }
        });
    });
});
