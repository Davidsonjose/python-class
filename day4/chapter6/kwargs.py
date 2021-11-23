# def states_capital(**kwargs):
#     print(kwargs)


# states_capital(imo= 'owerri', anabra= 'awka', lagos = 'ikeja')




def states_capital(**kwargs):
    for state, capital in kwargs.items():
        print(state+ ' <==>', capital)

states_capital(imo= 'owerri', abia= 'Umahia', adamawa= 'Yola')




