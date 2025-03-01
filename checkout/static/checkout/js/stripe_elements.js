/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Get Stripe public key and client secret from the script tags
var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.trim();
var client_secret = document.getElementById('id_client_secret').textContent.trim();

// Check if keys are loaded correctly
if (!stripe_public_key || !client_secret) {
    console.error("Stripe public key or client secret is missing!");
} else {
    var stripe = Stripe(stripe_public_key);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': { color: '#aab7c4' }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    var card = elements.create('card', { style: style });
    card.mount('#card-element');

    var cardValid = false;  // Track if card is entered correctly

    // Handle real-time validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            errorDiv.innerHTML = html;
            cardValid = false;
        } else if (event.empty) {
            errorDiv.innerHTML = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>Please enter your card details.</span>
            `;
            cardValid = false;
        } else {
            errorDiv.textContent = ''; // Clear error if card is valid
            cardValid = true;
        }
    });

    // Handle form submission with validation
    var form = document.getElementById('payment-form');
    var submitButton = document.getElementById('submit-button');
    var spinner = document.getElementById('spinner');

    function validateForm() {
        var isValid = true;

        // Check if the card field is filled
        if (!cardValid) {
            var cardErrors = document.getElementById('card-errors');
            if (!cardErrors.textContent.trim()) {
                cardErrors.innerHTML = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>Please enter your card details.</span>
                `;
            }
            isValid = false;
        }

        return isValid;
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent default form submission

        if (!validateForm()) {
            return; // Prevent submission if validation fails
        }

        submitButton.disabled = true;
        spinner.classList.remove("d-none");

        stripe.confirmCardPayment(client_secret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: document.getElementById('id_full_name').value,
                    email: document.getElementById('id_email').value
                }
            }
        }).then(function (result) {
            if (result.error) {
                document.getElementById('card-errors').textContent = result.error.message;
                submitButton.disabled = false;
                spinner.classList.add("d-none");
            } else {
                form.submit();
            }
        });
    });
}
