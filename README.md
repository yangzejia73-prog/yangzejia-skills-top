# Creator Skills CN / 自媒体创作 Skills

面向中文自媒体创作者的开源 Agent Skills 工具箱：把选题、资料研究、写作、跨平台改写与发布前风险检查，整理成可复用、可审查、可测试的工作流。

AI 可以加快创作，也可能带来虚构引用、事实失真、过度营销和危险自动化。本项目强调来源透明、事实与观点分离、最小权限和人工最终确认。

## Skills

| Skill | 用途 | 默认权限 |
|---|---|---|
| `topic-research` | 根据账号定位和受众形成可验证选题 | 无网络、Shell、文件写入 |
| `source-backed-outline` | 从用户提供的资料生成带证据状态的大纲 | 无网络、Shell、文件写入 |
| `xiaohongshu-draft` | 生成可人工编辑的小红书笔记 | 无网络、Shell、文件写入 |
| `wechat-article` | 生成结构清楚、来源透明的公众号长文 | 无网络、Shell、文件写入 |
| `content-repurpose` | 将一份母内容适配到多个平台 | 无网络、Shell、文件写入 |
| `content-risk-review` | 检查事实、隐私、高风险建议和夸大表达 | 无网络、Shell、文件写入 |

## 使用

将需要的 `skills/<name>` 文件夹复制到支持 Agent Skills 的工具中，或让 Agent 直接读取对应 `SKILL.md`。不同工具的安装方式可能不同，请以其官方文档为准。

示例请求：

```text
使用 topic-research，根据我的账号定位和目标读者提出 10 个选题。
不要把推测写成真实热度数据。
```

## 设计原则

- 不虚构来源、数据、案例、专家观点或平台规则。
- 资料不足时明确标注未知项和待核实项。
- 不以“爆款承诺”代替受众价值和事实质量。
- 默认不执行 Shell、不访问网络、不读写文件、不索取凭证。
- 发布、发送、删除、覆盖等外部操作始终需要用户明确授权。
- 医疗、金融、法律等高风险内容必须建议专业复核。

## 质量与安全检查

运行：

```bash
python scripts/validate_repository.py
```

验证器检查 Skill 元数据、必要章节、注册表一致性和常见危险指令。它不能替代人工安全审查。

## 贡献

欢迎提交真实使用案例、失败样例、平台适配和安全改进。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [SECURITY.md](SECURITY.md)。

## 状态

当前为 `v0.1.0` 初始公开版本。项目不声称已有下载量或广泛采用；使用反馈将通过 Issues、Pull Requests 和 Releases 公开记录。

## License

MIT
