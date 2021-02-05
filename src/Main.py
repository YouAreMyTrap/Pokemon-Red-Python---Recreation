from SQLCall_Log import *

print("Exist User: ", SQL().ConnectUser("user12", "0"))
SQL().NewUser("user12", "0")
print("Exist User: ", SQL().ConnectUser("user12", "0"))
SQL().RemoveUser("user12", "0")
print("Exist User: ", SQL().ConnectUser("user12", "0"))