// get text from checkout.html and slice the double commas from it
var print_js_file = "print Js File"

console.log('stripePublicKey  ---------***********-----------------**************------------');
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); //slice the double quotations

console.log(stripePublicKey)
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
console.log("stripe = ---------***********-----------------**************------------")
console.log(stripe)

var elements = stripe.elements()
console.log("elements = ---------***********-----------------**************------------")
console.log(elements)

var card = elements.create('card');
card.mount('#card-element')
console.log("card.mount ---------***********-----------------**************------------")
console.log(card.mount('#card-element'))

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    // event = {elementType: 'card', error: undefined, value: {…}, empty: false, complete: false, …}
    if (event.error) {
        // event.error = {code: 'invalid_number', type: 'validation_error', message: 'Your card number is invalid.'}
        var html = `
            <span class="icon" role="alert">
                <i class=''>i inside the event.error</i>
            </span>
            <span>${event.error.message}</span>'
        `;
        $(errorDiv).html(html)

    } else {
        errorDiv.textContent = '';
    }
});

// process:
// when hit the checkout page stripe create a payment intent
// Stripe returns client_secret, which is return to the template
// Use client_secret in the template to call confirmCardpayment() and verify the card number

// handle form submit