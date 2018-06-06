MAX_BEERS = 99
MIN_BEERS = 0

current_amount_of_beers = MAX_BEERS
message = '{} beczek piwa na polce stalo, jedna spadla {} zostalo'

while current_amount_of_beers > MIN_BEERS:
    print(message.format(current_amount_of_beers, current_amount_of_beers - 1))
    current_amount_of_beers -= 1