'''import numpy as np
import matplotlib.pyplot as plt
  
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12,19])
  
# number of observations/points
n = np.size(x)
  
# mean of x and y vector
m_x = np.mean(x)
m_y = np.mean(y)
  
# calculating cross-deviation and deviation about x
SS_xy = np.sum(y*x) - n*m_y*m_x
SS_xx = np.sum(x*x) - n*m_x*m_x
  
# calculating regression coefficients
b1 = SS_xy / SS_xx
b0 = m_y - b1*m_x 
b=(b0,b1)
print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))

# plotting the actual points as scatter plot
plt.scatter(x, y, color = "r",
               marker = "o", s = 30)
  
# predicted response vector
y_pred = b[0] + b[1]*x
  
# plotting the regression line
plt.plot(x, y_pred, color = "g")
  
# putting labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()'''




#gradent
import numpy as np 
import matplotlib.pyplot as plt 
  
class Linear_Regression: 
    def __init__(self, X, Y): 
        self.X = X 
        self.Y = Y 
        self.b = [0, 0] 
      
    def update_coeffs(self, learning_rate): 
        Y_pred = self.predict() 
        Y = self.Y 
        m = len(Y) 
        self.b[0] = self.b[0] - (learning_rate * ((1/m) *
                                np.sum(Y_pred - Y))) 
  
        self.b[1] = self.b[1] - (learning_rate * ((1/m) *
                                np.sum((Y_pred - Y) * self.X))) 
  
    def predict(self, X=[]): 
        Y_pred = np.array([]) 
        if not X: X = self.X 
        b = self.b 
        for x in X: 
            Y_pred = np.append(Y_pred, b[0] + (b[1] * x)) 
  
        return Y_pred 
      
    def get_current_accuracy(self, Y_pred): 
        p, e = Y_pred, self.Y 
        n = len(Y_pred) 
        return 1-sum( 
            [ 
                abs(p[i]-e[i])/e[i] 
                for i in range(n) 
                if e[i] != 0] 
        )/n 
#def predict(self, b, yi): 
  
    def compute_cost(self, Y_pred): 
        m = len(self.Y) 
        J = (1 / 2*m) * (np.sum(Y_pred - self.Y)**2) 
        return J 
  
    def plot_best_fit(self, Y_pred, fig): 
                f = plt.figure(fig) 
                plt.scatter(self.X, self.Y, color='b') 
                plt.plot(self.X, Y_pred, color='g') 
                f.show() 
  
  

X = np.array([i for i in range(10)]) 
Y = np.array([2*i for i in range(10)]) 
  
regressor = Linear_Regression(X, Y) 
  
iterations = 0
steps = 100
learning_rate = 0.02
costs = [] 
      
    #original best-fit line 
Y_pred = regressor.predict() 
regressor.plot_best_fit(Y_pred, 'Initial Best Fit Line') 
      
  
while 1: 
        Y_pred = regressor.predict() 
        cost = regressor.compute_cost(Y_pred) 
        costs.append(cost) 
        regressor.update_coeffs(learning_rate) 
          
        iterations += 1
        if iterations % steps == 0: 
            print(iterations, "epochs elapsed") 
            print("Current accuracy is :", 
                regressor.get_current_accuracy(Y_pred)) 
  
            stop = input("Do you want to stop (y/*)??") 
            if stop == "y": 
                break
  
#final best-fit line 
regressor.plot_best_fit(Y_pred, 'Final Best Fit Line') 
  
#plot to verify cost function decreases 
h = plt.figure('Verification') 
plt.plot(range(iterations), costs, color='b') 
h.show() 
  
# if user wants to predict using the regressor: 
regressor.predict([i for i in range(10)]) 
