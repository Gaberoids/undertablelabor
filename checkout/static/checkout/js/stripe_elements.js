// get text from checkout.html and slice the double commas from it
var print_js_file = "print Js File"
console.log(print_js_file);
console.log("stripe_elements.js inside ---------***********-----------------**************------------")
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); //slice the double quotations
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
    ;
// .addEventListener('change', function (event) { }