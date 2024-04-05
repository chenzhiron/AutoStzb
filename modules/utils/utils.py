import datetime
import numpy as np
from PIL import Image
from scipy.stats import truncnorm


def get_current_date(add_seconds=1):
    now = datetime.datetime.now()
    future_time = now + datetime.timedelta(seconds=add_seconds)
    return future_time


def calculate_max_timestamp(time_list):
    try:
        timestamp_list = []
        status = 0
        for times in time_list:
            try:
                dt = datetime.datetime.strptime(times, '%H:%M:%S')
                timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
                timestamp_list.append(timestamp)
            except Exception as e:
                status = 1
                timestamp_list.append(0)

        if sum(timestamp_list) == 0 and status == 0:
            return None
        return max(timestamp_list)
    except Exception as e:
        return None


def computedexecuteClickArea(xy):
    x = (xy[0] + xy[2]) / 2
    y = (xy[1] + xy[3]) / 2
    return x, y


def ocr_reg(res):
    if bool(res[0]):
        return [item[1][0] for sublist in res for item in sublist]
    else:
        return []


def generate_normal_distribution(ranges, sd=25):
    result = []
    for low, high in ranges:
        mean = (low + high) / 2.0
        data = truncnorm(
            (low - mean) / sd,  # 下截断点
            (high - mean) / sd,  # 上截断点
            loc=mean,
            scale=sd).rvs()
        result.append(int(data))
    return result


def blackout_image_except_region(image_path, region):
    """
    Black out a region of an image except for the specified area.

    Parameters:
    - image_path: str, the path to the image that should be processed.
    - region: tuple, a 4-tuple specifying the left, upper, right, and lower pixel coordinate.

    Returns:
    - An Image object with the region outside the specified area blacked out.
    """
    # Load the original image
    original_image = Image.open(image_path)

    # Create a black image of the same size as the original image
    black_image = Image.new('RGB', original_image.size, 'black')

    # Crop the specified region from the original image
    cropped_region = original_image.crop(region)

    # Paste the cropped region onto the black image at the same coordinates
    black_image.paste(cropped_region, region)

    return black_image


def blackout_image_except_region_efficient(image_path, region):
    """
    Black out a region of an image except for the specified area, more efficiently.

    Parameters:
    - image_path: str, the path to the image that should be processed.
    - region: tuple, a 4-tuple specifying the left, upper, right, and lower pixel coordinate.

    Returns:
    - An Image object with the region outside the specified area blacked out.
    """
    # Load the original image
    original_image = Image.open(image_path)

    # Convert the image into a NumPy array for faster processing
    img_array = np.array(original_image)

    # Extract the coordinates from the region
    left, upper, right, lower = region

    # Create a mask for the area to blackout
    mask = np.ones_like(img_array, dtype=bool)  # Create a mask initialized to True
    mask[upper:lower, left:right] = False  # Set the region to keep to False

    # Apply the mask to black out regions
    img_array[mask] = 0  # Set the True areas of the mask to black

    # Convert the NumPy array back to a PIL Image
    blacked_out_image = Image.fromarray(img_array)

    return blacked_out_image
