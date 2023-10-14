def predict_objects(image_location, save=True):
    from ultralytics import YOLO

    model = YOLO('best.pt')
    model.predict(image_location, save=save)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Object Detection")
    parser.add_argument('image_location', help="Path to the input image")
    parser.add_argument('--save', action="store_true", help="Save the prediction results")

    args = parser.parse_args()
    predict_objects(args.image_location, save=args.save)
