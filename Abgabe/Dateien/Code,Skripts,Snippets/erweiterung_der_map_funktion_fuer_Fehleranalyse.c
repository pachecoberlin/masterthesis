void draw_and_save_wrong_images(void checkpoint_detections_count, void detections_count, int num_labels, int t, int val,
		box* truth, void nboxes, detection* dets, float thresh_calc_avg_iou, char* path, int fp) {
	int i, j;
	//Draw labels and detection boxes
	for (j = 0; j < num_labels; ++j) {
		box tb = { truth[j].x, truth[j].y, truth[j].w, truth[j].h };
		draw_bbox(val[t], tb, 2, 0.0, 1.0, 0.0);
	}
	for (i = 0; i < nboxes; ++i) {
		if (dets[i].prob[0] > thresh_calc_avg_iou) {
			draw_bbox(val[t], dets[i].bbox, 2, 1.0, 0.0, 0.0);
		} else if (dets[i].prob[0] > 0) {
			draw_bbox(val[t], dets[i].bbox, 2, 0.0, 0.0, 1.0);
		}
	}
	//set correct path
	int actual_detections = detections_count - checkpoint_detections_count;
	if (actual_detections < num_labels) {
		find_replace(path, "/images/", "/false/falsenegative/", path);
		find_replace(path, ".jpg", "_FN", path);
		find_replace(path, ".png", "_FN", path);
	} else if (actual_detections > num_labels && !fp) {
		find_replace(path, "/images/", "/false/others/", path);
		find_replace(path, ".jpg", "_false", path);
		find_replace(path, ".png", "_false", path);
	} else if (fp) {
		find_replace(path, "/images/", "/false/falsepositives/", path);
		find_replace(path, ".jpg", "_FP", path);
		find_replace(path, ".png", "_FP", path);
	} else {
		return;
	}
	save_image(val[t], path);
}
