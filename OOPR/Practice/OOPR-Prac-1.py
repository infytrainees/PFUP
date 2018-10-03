#OOPR-Prac-1
#Start writing you code here
class Purchase:
    list_of_items = ["cake","soap","jam","cereal","hand sanitizer","biscuits","bread"]
    list_of_count_of_each_item_sold = [0,0,0,0,0,0,0]
    def __init__(self):
        self.__items_purchased=[]
        self.__item_on_offer=None

    def get_items_purchased(self):
        return self.__items_purchased

    def get_item_on_offer(self):
        return self.__item_on_offer

    def sell_items(self,list_of_items_to_be_purchased):
        for item_purchased in list_of_items_to_be_purchased:
            
            for available_items in Purchase.list_of_items:
                
                if item_purchased.lower() == available_items.lower():
                    if item_purchased.lower() == "soap":
                        self.provide_offer()
                    indx = Purchase.list_of_items.index(available_items)
                    self.__items_purchased.append(available_items)
                    Purchase.list_of_count_of_each_item_sold[indx] += 1 
                    break
                     
    def provide_offer(self):
        for x in Purchase.list_of_items:
            if x.lower() == "hand sanitizer":
                indx = Purchase.list_of_items.index(x)
                break
        Purchase.list_of_count_of_each_item_sold[indx]+=1
        self.__item_on_offer='HAND SANITIZER'
    
    @staticmethod
    def find_total_items_sold():
        return sum(Purchase.list_of_count_of_each_item_sold)
