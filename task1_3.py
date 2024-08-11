
def main():
    request_spending = {
    "Mahek": {
    "balance": 3000.00,
    "transactions": [
    {"amount": -9000.00, "category": "Creatives"},
    {"amount": 7000.00, "category": "Sponsor"},
    {"amount": -2000.00, "category": "Prize-Money"}]
    },
    "Arham": {
    "balance": 5000.00,
    "transactions": [
    {"amount": 8000.00, "category": "Stalls"},
    {"amount": 7500.00, "category": "Seminars"}
    ]
    },
    "Unnati": {
    "balance": 3500.00,
    "transactions": [
    {"amount": -5000.00, "category": "Attraction"},
    {"amount": 2500.00, "category": "Promo"},
    {"amount": -900.00, "category": "Lighting"}, {
    "amount":-3000.00, "category": "Games"}]

    },
    "Gaurang": {
    "balance": 2000.00,
    "transactions": [
    {"amount": 1500.00, "category": "Website"}, {"amount": 1000.00, "category": "C2C"},
    {"amount": -500.00, "category": "Posters"}]
    }
    }
    
    id = input("Enter the account id whoes amount you want to find : ")
    category = input("Enter the catogary whoes amount you want to find : ")
    amount = total_spending(request_spending,id,category)
    print("amount paid by "+id +"in"+ category +" is "+ str(amount))
    account_balance(request_spending,id)
    val = account_balance(request_spending,id)
    print(f"Balance of {id} is {val}")
    money_owed(request_spending ,id )

    



def total_spending(request_spending,account_id,catagory):
    transaction = request_spending.get(account_id).get("transactions")
    for each_line in transaction:
        if(each_line.get("category")==catagory):
            return int(each_line.get("amount"))
        

def account_balance(request_spending,account_id):
    transaction = request_spending.get(account_id).get("transactions")
    money=0
    for entry in transaction:
        money =money + entry.get("amount")
    money = -money
    val = request_spending.get(account_id).get("balance")  -  money
    return val 
    

def money_owed(request_spending , account_id ):
    ans = account_balance(request_spending,account_id)
   # left = request_spending.get(account_id).get("balance")  -  ans ans = -1000 money given to her shd be 1000rs and ans=+1000 she has to give back
    if(ans>0):
        print(f"{account_id} has to pay back { ans} to the trasurer")
    else:
        print(f"The treasurer needs to give her money rs: { ans}" ) # how much extra money needed to be given 
        


main()


                
                
    





