from pathlib import Path
from typing import Dict

import cv2


class ImgNames:
    IMGS_DIR = Path(__file__).parent.parent / "imgs"
    _IMAGE_CACHE: Dict[str, any] = {}  # 图片缓存字典

    # 战斗相关
    ATTACK = "attack_template"
    DEFEND = "defend_template"
    SHILI = 'shili'
    SHILIPAGE = "shili_page"
    ZHENGBING = "zhengbing"
    ZHENGBINGING = "zhengbinging"
    ZHENGBINGMAX = 'zhengbing_max'
    SEARCH = 'search'
    JINGON = 'jingon'
    SAODANG = 'saodang'
    ACTIONREQUIRE = 'action_require'
    ACTIONLIST = 'action_list'
    ADDRESS = 'address'
    @classmethod
    def get_path(cls, img_name: str, ext: str = ".png") -> str:
        """根据常量获取图片完整路径"""
        path = cls.IMGS_DIR / f"{img_name}{ext}"
        if not path.exists():
            raise FileNotFoundError(f"图片不存在: {path}")
        return str(path)

    @classmethod
    def get_image(cls, img_name: str, ext: str = ".png") -> any:
        """获取图片对象，使用缓存"""
        cache_key = f"{img_name}{ext}"

        # 如果图片已在缓存中，直接返回
        if cache_key in cls._IMAGE_CACHE:
            return cls._IMAGE_CACHE[cache_key]

        path = cls.get_path(img_name, ext)
        img = cv2.imread(path)  # 使用OpenCV读取图片，根据需要可以替换为其他库
        if img is None:
            raise ValueError(f"无法加载图片: {path}")

        cls._IMAGE_CACHE[cache_key] = img
        return img


if __name__=='__main__':
    attack = ImgNames.get_path(ImgNames.ZHENGBINGING)
    print(attack)