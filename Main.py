from SQLCall_Log import *

SqlBase = SQL()
print("Exist User: ", SqlBase.ConnectUser("user12", "0"))
SqlBase.NewUser("user12", "0")
print("Exist User: ", SqlBase.ConnectUser("user12", "0"))
SqlBase.RemoveUser("user12", "0")
print("Exist User: ", SqlBase.ConnectUser("user12", "0"))