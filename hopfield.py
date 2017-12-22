import converter


def calc(train_files, test_files, a=0.5, time=1000, size=(100, 100), threshold=60, current_path=None):
  global weights_matrix
  files_count = 0
  for train_file_path in train_files:
    x_matrix = converter.image_to_array(file_path=train_file_path, size=size, threshold=threshold)
    x_vector = converter.matrix_to_vector(x_matrix)
    if files_count == 0:
      weights_matrix = converter.create_weights_matrix(x_vector)
      files_count = 1
    else:
      weights_buffer = converter.create_weights_matrix(x_vector)
      weights_matrix = weights_matrix + weights_buffer
      files_count += 1

  result_image_counter = 0
  for test_file_path in test_files:
    y_matrix = converter.image_to_array(file_path=test_file_path, size=size, threshold=threshold)
    y_matrix_dimensions = y_matrix.shape
    y_vector = converter.matrix_to_vector(y_matrix)
    y_result_vector = converter.update(w=weights_matrix, y_vec=y_vector, sizes=y_matrix_dimensions, theta=a, time=time)
    y_result_vector = y_result_vector.reshape(y_matrix_dimensions)
    if current_path is not None:
      out_file = current_path + "/result" + "/result_" + str(result_image_counter) + ".jpeg"
      converter.array_to_image(y_result_vector, output_file=out_file)
      result_image = converter.array_to_image(y_result_vector, output_file=None)
      result_image.show()
    else:
      result_image = converter.array_to_image(y_result_vector, output_file=None)
      result_image.show()
    result_image_counter += 1
