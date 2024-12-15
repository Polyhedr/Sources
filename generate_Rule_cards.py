import os
import glob
from pathlib import Path
import cv2
import argparse
import numpy as np
bp=breakpoint

def get_args():
    parser = argparse.ArgumentParser(description="Run lualatex on .tex files in a directory tree.")
    parser.add_argument(
        "--dpi",
        type=int,
        default=900,
        help="dots per inch"
    )
    parser.add_argument(
        "--padding",
        type=str,
        default='6.1 mm',
        help="white padding in mm"
    )
    parser.add_argument(
        "--output",
        type=str,
        default='output',
        help="output folder"
    )
    return parser.parse_args()

def draw_rounded_rectangle(image, top_left=None, bottom_right=None, color=(255,255,255,255), corner_radius=None, thickness=None, stroke_color=(100,100,100,255)):
    # Unpack corners
    if not thickness:
        thickness = int(image.shape[1]*.005) * 2
    if not top_left:
        top_left = (int(thickness/2), int(thickness/2))
    if not bottom_right:
        bottom_right = (image.shape[1]-int(thickness/2), image.shape[0]-int(thickness/2))
    x1, y1 = top_left
    x2, y2 = bottom_right
    if not corner_radius:
        corner_radius = int(image.shape[1] * .1)

    # Adjust radius if too large
    corner_radius = min(corner_radius, (x2 - x1) // 2, (y2 - y1) // 2)

    # Center rectangle
    cv2.rectangle(image, (x1 + corner_radius, y1), (x2 - corner_radius, y2), color, -1)
    cv2.rectangle(image, (x1, y1 + corner_radius), (x2, y2 - corner_radius), color, -1)

    # Corner circles
    cv2.circle(image, (x1 + corner_radius, y1 + corner_radius), corner_radius, color, -1)
    cv2.circle(image, (x2 - corner_radius, y1 + corner_radius), corner_radius, color, -1)
    cv2.circle(image, (x1 + corner_radius, y2 - corner_radius), corner_radius, color, -1)
    cv2.circle(image, (x2 - corner_radius, y2 - corner_radius), corner_radius, color, -1)
    if thickness>0:
        # Outer lines
        cv2.line(image, (x1 + corner_radius, y1), (x2 - corner_radius, y1), stroke_color, thickness)
        cv2.line(image, (x1 + corner_radius, y2), (x2 - corner_radius, y2), stroke_color, thickness)
        cv2.line(image, (x1, y1 + corner_radius), (x1, y2 - corner_radius), stroke_color, thickness)
        cv2.line(image, (x2, y1 + corner_radius), (x2, y2 - corner_radius), stroke_color, thickness)

        # Corner arcs
        cv2.ellipse(image, (x1 + corner_radius, y1 + corner_radius), (corner_radius, corner_radius), 180, 0, 90, stroke_color, thickness)
        cv2.ellipse(image, (x2 - corner_radius, y1 + corner_radius), (corner_radius, corner_radius), 270, 0, 90, stroke_color, thickness)
        cv2.ellipse(image, (x1 + corner_radius, y2 - corner_radius), (corner_radius, corner_radius), 90, 0, 90, stroke_color, thickness)
        cv2.ellipse(image, (x2 - corner_radius, y2 - corner_radius), (corner_radius, corner_radius), 0, 0, 90, stroke_color, thickness)

    return image

def main(dpi, padding, output_folder):
    for rule_path in sorted(glob.glob(os.path.join("rules","*","*",'rule.tex'))):
        game_path = Path(rule_path).parent

        # get the pdf with lualatex
        os.system(fr"cd {game_path};lualatex rule.tex")

        # convert the pdf to png with ImageMagick
        os.system(f"convert -density {dpi} {rule_path.replace('.tex','.pdf')} -quality 100 {rule_path.replace('.tex','.png')}")
        os.system(f"magick convert -density {dpi} {rule_path.replace('.tex','.pdf')} -quality 100 {rule_path.replace('.tex','.png')}")

        # get the top part of the card for the README
        crop = cv2.imread(rule_path.replace('.tex','-0.png'), cv2.IMREAD_UNCHANGED)[int(4.87 * dpi / 25.4):int(24.2 * dpi / 25.4),int(20.2 * dpi / 25.4):int(60 * dpi / 25.4),:]
        crop, alpha_layer = crop[:,:,:3], crop[:,:,3:]/255
        rounded_rectangle = draw_rounded_rectangle(np.zeros((crop.shape[0] + 2*int(3 * dpi / 25.4), crop.shape[1] + 2*int(2 * dpi / 25.4),4)))
        rounded_rectangle[int(3 * dpi / 25.4):-int(3 * dpi / 25.4), int(2 * dpi / 25.4):-int(2 * dpi / 25.4), :3] = crop[:, :, :3] * alpha_layer + 255*(1 - alpha_layer)
        cv2.imwrite(rule_path.replace('.tex','_top.png'), rounded_rectangle)

        # generate the card with white padding
        for card_side_path in glob.glob(rule_path.replace('.tex', '*-*.png')):
            card_side = cv2.imread(card_side_path, cv2.IMREAD_UNCHANGED)
            card_side, alpha_layer = card_side[:,:,:3], card_side[:,:,3:]/255
            pixel_height, pixel_width = card_side.shape[:2]
            canvas = 255*np.ones((pixel_height + 2*padding, pixel_width + 2*padding, 3), dtype=np.uint8)
            canvas[padding:-padding,padding:-padding] = card_side * alpha_layer + canvas[padding:-padding,padding:-padding] * (1 - alpha_layer)
            cv2.imwrite(os.path.join(output_folder, Path(card_side_path).stem + '-' + game_path.stem + '.png'), canvas)
            os.system(f'rm {card_side_path}')

if __name__ == "__main__":
    args = get_args()
    os.makedirs(args.output, exist_ok=True)
    main(args.dpi, int(.5*float(args.padding.replace(' mm','')) * args.dpi / 25.4), args.output)
    print('Done')
        
