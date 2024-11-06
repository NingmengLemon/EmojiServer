# EmojiServer

因为 [pilmoji](https://github.com/jay3332/pilmoji) 用的 CDN 在大陆地区死活连不上所以打算自己部署一个，但是又不想跑 npm，于是用 py 写了一个

数据部分基本照搬了 [emojicdn](https://github.com/benborgers/emojicdn/blob/main/index.ts)

如果后续闲的话大概会把它的功能补全（大概）

直接使用的话需要把 [emoji-data](https://github.com/iamcal/emoji-data) 下的 `img-google-136` 文件夹 和 `emoji.json` 复制过来，不想放在同一目录下的话还需要给 `src/emojiserver/server.py` 中 `EmojiDataset` 初始化的时候补传一下路径参数

因为时效性的问题就没把数据文件弄进仓库里，要部署的话需要自己复制一下，什么的
