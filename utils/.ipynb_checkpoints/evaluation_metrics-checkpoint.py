import tensorflow as tf

def compute_mmd(x, y, sigma=1.0):
    """
    Compute the Maximum Mean Discrepancy (MMD) between two samples.

    Args:
        x: np.array or tensor, first dataset (n_samples, n_features)
        y: np.array or tensor, second dataset (n_samples, n_features)
        sigma: float, bandwidth parameter for the RBF kernel

    Returns:
        mmd_score: float, the MMD value between x and y
    """
    x = tf.convert_to_tensor(x, dtype=tf.float32)
    y = tf.convert_to_tensor(y, dtype=tf.float32)

    # Compute Gram matrices
    xx = tf.matmul(x, tf.transpose(x))
    yy = tf.matmul(y, tf.transpose(y))
    xy = tf.matmul(x, tf.transpose(y))

    rx = tf.expand_dims(tf.reduce_sum(x * x, axis=1), 0)
    ry = tf.expand_dims(tf.reduce_sum(y * y, axis=1), 0)

    Kxx = tf.exp(- (rx - 2 * xx + tf.transpose(rx)) / (2 * sigma ** 2))
    Kyy = tf.exp(- (ry - 2 * yy + tf.transpose(ry)) / (2 * sigma ** 2))
    Kxy = tf.exp(- (rx - 2 * xy + tf.transpose(ry)) / (2 * sigma ** 2))

    # Compute MMD
    mmd_score = tf.reduce_mean(Kxx) + tf.reduce_mean(Kyy) - 2 * tf.reduce_mean(Kxy)

    return mmd_score.numpy()
