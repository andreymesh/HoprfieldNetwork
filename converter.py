import numpy as np
import random
import os
from PIL import Image


def matrix_to_vector(input_matrix):
  vector_size = input_matrix.shape[0] * input_matrix.shape[1]
  vector = np.zeros(vector_size)

  iterator_index = 0
  for row_index in range(input_matrix.shape[0]):
    for column_index in range(input_matrix.shape[1]):
      vector[iterator_index] = input_matrix[row_index, column_index]
      iterator_index += 1
  return vector


def create_weights_matrix(input_vector):
  input_vector_dimension = len(input_vector.shape)
  input_vector_length = len(input_vector)
  if input_vector_dimension != 1:
    print("The input vector is not a vector")
    return
  else:
    weights_matrix = np.zeros([input_vector_length, input_vector_length])
    for row_index in range(input_vector_length):
      for column_index in range(row_index, input_vector_length):
        if row_index == column_index:
          weights_matrix[row_index, column_index] = 0
        else:
          weights_matrix[row_index, column_index] = input_vector[row_index] * input_vector[column_index]
          weights_matrix[column_index, row_index] = weights_matrix[row_index, column_index]
  return weights_matrix


def image_to_array(file_path, size, threshold=145):
  read_image = Image.open(file_path)
  converted_image = read_image.convert(mode="L")
  result_image = converted_image.resize(size)
  image_array = np.asarray(result_image, dtype=np.uint8)
  result_array = np.zeros(image_array.shape, dtype=np.float)
  result_array[image_array > threshold] = 1
  result_array[result_array == 0] = -1
  return result_array


def array_to_image(input_matrix, output_file=None):
  y = np.zeros(input_matrix.shape, dtype=np.uint8)
  y[input_matrix == 1] = 255
  y[input_matrix == -1] = 0
  result_image = Image.fromarray(y, mode="L")
  if output_file is not None:
    result_image.save(output_file)
  return result_image


def update(w, y_vec, sizes, theta=0.5, time=100):
  m = len(y_vec)
  # result_image_counter = 0
  for s in range(time):
    # out_file = os.getcwd() + "/result" + "/result_" + str(s) + ".jpeg"
    i = random.randint(0, m - 1)
    u = np.dot(w[i][:], y_vec) - theta

    if u > 0:
      y_vec[i] = 1
    elif u < 0:
      y_vec[i] = -1

    # imgArray = y_vec.reshape(sizes)
    # array_to_image(imgArray, output_file=out_file)


  return y_vec
