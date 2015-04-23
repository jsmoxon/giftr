import os
import stripe

stripe_keys = {
	'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

def stripe_charge(dollar_amount, stripe_token, email, description):
	amount_in_cents = dollar_amount * 100
	customer = stripe.Customer.create(
		email=email,
		card=stripe_token
		)

	charge = stripe.Charge.create(
		customer=customer.id,
        amount=amount_in_cents,
        currency='usd',
        description=description
		)
	return 