import tensorflow as tf

hello = tf.constant('Hello Kenge')
sess = tf.Session()
print (sess.run(hello))