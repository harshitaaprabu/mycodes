sample_dict={"Name":"Harshitaa","Age":18,"College":"SRM","Phone":9876897657,"Education":["BCA","ME","PHD"],"Mrital Status":False}
print(sample_dict["Age"])
print(sample_dict["Education"][2])
print(sample_dict.get("Address",23))
sample_dict["Address"]="17,Thiruvanmiyur,Chennai"
print(sample_dict["Address"][17:24])
print(sample_dict["Address"].split(",")[2])
