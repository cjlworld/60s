基于机器人的钉钉早报推送

> 早报来自 ALAPI 的 [每日60秒早报-ALAPI](https://www.alapi.cn/api/view/93) 

### 使用方法

1. 先 Fork 整个项目
2. 注册 ALAPI 账号，获取 token，在 settings/secret 中加入新的 secret `ALAPI_TOKEN` ，值为获取的 TOKEN。
3. 在需要推送早报的钉钉群中加入 webhook 机器人，安全设置为加签。
   - 密钥填入 新的 secret `DING_SECRET` 
   - webhook 填入 新的 secret `DING_WEBHOOK` 
4. 在 `run.yml`  中修改时间（默认 每日早晨 7:10 ）即可