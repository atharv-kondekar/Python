import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

X=np.array([
        [7.8 , 120],
        [6.5 , 110],
        [8.2 , 130],
        [5.0 , 100],
        [7.0 , 105]
            ])
Y=np.array([[1],[0],[1],[0],[0]])

np.random.seed(1)
input_layer=X.shape[1]
#Multiple_hidden layer
hidden_layer1=4
hidden_layer2=3
output_layer=1


w1=np.random.randn(input_layer,hidden_layer1)
b1=np.random.randn(1,hidden_layer1)

w2=np.random.randn(hidden_layer1,hidden_layer2)
b2=np.random.randn(1,hidden_layer2)

w3=np.random.randn(hidden_layer2,output_layer)
b3=np.random.randn(1,output_layer)


def feedForward(x,w1,w2,b1,b2):
    input_function1=np.dot(x,w1)+b1
    final_input1=sigmoid(input_function1)
    
    input_function2=np.dot(input_function1,w2)+b2
    final_input2=sigmoid(input_function2)
    
    
    output_function=np.dot(final_input2,w3)+b3
    final_output=sigmoid(output_function)
    
    return final_output

new_student=np.array([[7.5,115]])

placement_probablity=feedForward(new_student,w1,w2,b1,b2)


print("The Predicted Probility : ",placement_probablity[0][0])
if placement_probablity[0][0] >0.5 :
    print(" Placed")
else:
    print(" Not Placed")
    
