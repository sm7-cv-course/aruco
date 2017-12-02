#include_directories(
  #${CMAKE_CURRENT_SOURCE_DIR}
  #${CMAKE_CURRENT_BINARY_DIR}
#)

#include_directories ("${CMAKE_CURRENT_SOURCE_DIR}/source")

add_executable (aruco_calib
	            calibrator.cpp)

target_link_libraries (aruco_calib ${ADDON_LIBRARIES} ${OpenCV_LIBS})

