class CementDealer:
    def getCementCost(self,quentity):
        return quentity*300

class IronDealer:
    def getIronCost(self,quentity):
        return quentity*4500

class Builder(CementDealer,IronDealer):
    def getTotalCost(self,cQ,iQ):
        c_cost=self.getCementCost(cQ)
        i_cost=self.getIronCost(iQ)
        totalCost=c_cost+i_cost
        return totalCost
    
cement=int(input("Enter Cement Quentity:"))
iron=int(input("Enter Iron Quentity:"))

b=Builder()

total_cost=b.getTotalCost(cement,iron)
print("TOTAL COST:",total_cost)
