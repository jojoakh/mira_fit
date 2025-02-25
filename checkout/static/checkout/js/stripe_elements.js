/*
    Stripe Payment Processing
    Based on Stripe's official documentation:
    https://stripe.com/docs/payments/accept-a-payment
*/

// Get Stripe public key and client secret from the template
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim();
var clientSecret = document.getElementById('id_client_secret').textContent.trim();

// Initialize Stripe.js
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Define styling for the Stripe card input
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create and mount Stripe card element
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function(event) {
    var errorDisplay = document.getElementById('card-errors');
    if (event.error) {
        errorDisplay.textContent = event.error.message;
    } else {
        errorDisplay.textContent = '';
    }
});

// Handle form submission
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Disable submit button to prevent multiple clicks
    var submitButton = document.getElementById('submit-button');
    submitButton.disabled = true;

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value,
                email: form.email.value,
                phone: form.phone_number.value
            }
        }
    }).then(function(result) {
        if (result.error) {
            // Display error message
            var errorDisplay = document.getElementById('card-errors');
            errorDisplay.textContent = result.error.message;
            submitButton.disabled = false; // Re-enable submit button
        } else {
            // Payment successful - submit the form
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
