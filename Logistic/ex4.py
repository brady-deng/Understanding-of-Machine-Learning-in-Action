import ex3
import tensorflow as tf
import numpy as np
data_train,label_train,data_test,label_test = ex3.load_data()
data_train = np.mat(data_train)
data_test = np.mat(data_test)
# NUM_ite = int(input("Please input the number of train step:"))
NUM_ite = 1000
temp_test = []
temp_train = []
for num in label_test:
    temp_test.append(int(num))
for num in label_train:
    temp_train.append(int(num))
# sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32,[None,21])
y_ = tf.placeholder(tf.float32,[None,2])
w1 = tf.Variable(tf.ones([21,5]))
b1 = tf.Variable(tf.zeros([5]))
y1 = tf.nn.sigmoid(tf.matmul(x,w1)+b1)
w2 = tf.Variable(tf.ones([5,5]))
b2 = tf.Variable(tf.zeros([5]))
y2 = tf.nn.sigmoid(tf.matmul(y1,w2)+b2)
w3 = tf.Variable(tf.ones([5,2]))
b3 = tf.Variable(tf.zeros([2]))
y = tf.nn.softmax(tf.matmul(y2,w3)+b3)
cross_entropy = -tf.reduce_sum(tf.reduce_sum(y_*tf.log(y)))
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
sess = tf.Session()
init = tf.global_variables_initializer()

sess.run(init)
label_train = sess.run(tf.one_hot(temp_train,2,1,0))
label_test = sess.run(tf.one_hot(temp_test,2,1,0))


for i in range(NUM_ite):
    batch_x = data_train
    batch_y = label_train

    sess.run(train_step,feed_dict={x:batch_x,y_:batch_y})
    if i % 50 == 0:
        result = sess.run(accuracy,feed_dict={x:data_test,y_:label_test})
        print("The accuracy of the prediction is: %s" % result)

