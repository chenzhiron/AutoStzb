from pathlib import Path


class ImgNames:
    IMGS_DIR = Path(__file__).parent.parent / "imgs"


    # 战斗相关
    ATTACK = "attack_template"
    DEFEND = "defend_template"
    SHILI = 'shili'
    SHILIPAGE ="shili_page"
    ZHENGBING="zhengbing"
    ZHENGBINGING="zhengbinging"
    ZHENGBINGMAX='zhengbing_max'
    SEARCH = 'search'

    @classmethod
    def get_path(cls, img_name: str, ext: str = ".png") -> str:
        """根据常量获取图片完整路径"""
        path = cls.IMGS_DIR / f"{img_name}{ext}"
        if not path.exists():
            raise FileNotFoundError(f"图片不存在: {path}")
        return str(path)


if __name__=='__main__':
    attack = ImgNames.get_path(ImgNames.ZHENGBINGING)
    print(attack)