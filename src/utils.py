# A stellar function that return list of all operation on an acc and the sum
from stellar_sdk import Server, TransactionBuilder, server

# horizon_url = "https://horion-testnet.stellar.org"
horizon_url = "https://horizon.stellar.org"
main_server = Server(horizon_url=horizon_url)



def sum_of_all_operation_on_a_stellar_acct(pub_key :str):
    all_operations_getter = main_server.operations().for_account(pub_key).order(desc=False).limit(200)
    page_counter = 0
    next_ops = all_operations_getter.call()
    while len(next_ops["_embedded"]['records']) == 200:
        page_counter += len(next_ops["_embedded"]['records'])
        next_ops_again  = all_operations_getter.next()
        print(page_counter)
        page_counter += len(next_ops_again["_embedded"]['records'])
        if len(next_ops_again["_embedded"]['records']) < 200:
            break

    return page_counter


adc = sum_of_all_operation_on_a_stellar_acct("GAZOBJBNS3R4ZFJNNXCM46P2YQOYYZX6B6AWTOTE5GCG53ZMYHWKWKIB")
print(adc)