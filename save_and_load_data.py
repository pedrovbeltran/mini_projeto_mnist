import json

# Saving results on a file - Functions
def save_data(filename, test_accuracy, acc_by_class, \
              epochs, no_improvement_in, mbs, eta):
    data = {"test_accuracy": test_accuracy,
            "acc_by_class": acc_by_class,
            #"cost": evaluation_cost,
            "eta": eta,
            "mini-batch size": mbs,
            "epochs": epochs,
            "no_improvement_in": no_improvement_in}

    f = open(filename, "w")
    json.dump(data, f)
    f.close()

#*************************************

# Loading results from a file
def load_data(filename):
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    return data
#*************************************
