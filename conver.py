import tensorflow as tf

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('./artifacts2/fns.ckpt.meta')
    saver.restore(sess, "/artifacts2/fns.ckpt.data-00000-of-00001")

print("is this a success?")
