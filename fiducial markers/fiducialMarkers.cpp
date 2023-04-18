
using namespace cv;

int main()
{
    cv::Mat markerImage;
    cv::aruco::Dictionary dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);
    cv::aruco::generateImageMarker(dictionary, 23, 200, markerImage, 1);
    cv::imwrite("marker23.png", markerImage);
}