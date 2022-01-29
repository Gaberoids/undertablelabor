// get text from checkout.html and slice the double commas from it
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); //slice the double quotations
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// next line is used to set up stripe
var stripe = Stripe(stripePublicKey);
console.log("stripe = ---------***********-----------------**************------------")
console.log(stripe)
// above this is a dictionary of a bunch of objects from stripe like confirmCardNumber:ƒ (r,a), confirmIdentity:ƒ (r,a), etc, All empty at this point

// below is the creating of a instance of stripe elements
var elements = stripe.elements();
console.log("elements = ---------***********-----------------**************------------")
console.log(elements)
// this is list of functions or dictionary  from stripe like update ƒ (r,a), create ƒ (r,a) etc.

// style for the card element coming next
var style = {
    base: {
        color: '#FFFF00',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: 'purple'
        }
    },
    invalid: {
        color: 'green',
        iconColor: '#FFFF00'
    }
};

// creating the element card
var card = elements.create('card', {style: style});
console.log(card)
// console.log shows a bunch of objects addEventListener: ƒ (r,a), addListener: ƒ(r, a), blur: ƒ(r), clear: ƒ(r)

// mount the card element to the dive ID below #card_element
card.mount('#card-element');
// console shows 'undefined' for console.log(card.mount('#card-element')
console.log(card.mount('#card-element'));

// this listener function is to add error message when card number is invalid
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
// the listener will preventDefault action
// this will make sure the card number will go to stripe securely
FormData.addEventListener('submit', function (ev) {
    ev.preventDefault();
    // below is meant to prevent multiple submitions    
    card.update(('disabled'))
    $('#submit-button').attr('disabled, true');
    // this below send the card information securilly to stripe
    stripe.confirmCardPayment(clientSecret, {
        // below is to store payment information to be used with stripe
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
            }
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
            <span class="icon" role="alert">
                <i class=''>i inside the event.error</i>
            </span>
            <span>${result.error.message}</span>'
            `;
            $(errorDiv).html(html)
            // below is meant to reenabled the buttons submitted    
            card.update(('disabled'))
            $('#submit-button').attr('disabled, true');
        } else {
            form.submit()
        }
    })
})
