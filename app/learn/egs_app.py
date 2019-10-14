#
import tensorflow as tf
from ann.learn.egs_model import EgsModel

class EgsApp(object):
    def __init__(self):
        self.name = 'app.EgsApp'

    @staticmethod
    @tf.function
    def train_step(model, optimizer, loss_object, images, labels, train_loss, train_accuracy):
        with tf.GradientTape() as tape:
            predictions = model(images)
            loss = loss_object(labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        train_loss(loss)
        train_accuracy(labels, predictions)

    def startup(self):
        print('Expert Getting Start App v0.0.1')
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0
        x_train = x_train[..., tf.newaxis]
        x_test = x_test[..., tf.newaxis]
        train_ds = tf.data.Dataset.from_tensor_slices(
                    (x_train, y_train)).shuffle(10000).batch(32)
        test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)
        model = EgsModel()
        loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
        optimizer = tf.keras.optimizers.Adam()
        train_loss = tf.keras.metrics.Mean(name='train_loss')
        train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
        test_loss = tf.keras.metrics.Mean(name='test_loss')
        test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')
        @tf.function
        def test_step(images, labels):
            predictions = model(images)
            t_loss = loss_object(labels, predictions)
            test_loss(t_loss)
            test_accuracy(labels, predictions)
        EPOCHS = 5
        for epoch in range(EPOCHS):
            for images, labels in train_ds:
                EgsApp.train_step(model, optimizer, images, labels, train_loss, train_accuracy)
            for test_images, test_labels in test_ds:
                test_step(test_images, test_labels)
            template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
            print (template.format(epoch+1,
                         train_loss.result(),
                         train_accuracy.result()*100,
                         test_loss.result(),
                         test_accuracy.result()*100))