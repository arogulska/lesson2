def get_sum(num_one, num_two):
    try:
        result = int(num_one) + int(num_two)
        print(result)
    except ValueError:
        print ("Try again!")

get_sum(1, "one")

