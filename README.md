# mkdocs-ruby-plugin

An MkDocs plugin to add pinyin/furigana to Chinese/Japanese Kanji text.

It's based on https://github.com/ijaureguialzo/mkdocs-furigana-plugin, but replace CSS style with HTML `<ruby>` tag.


## Installation

```
pip3 install mkdocs-ruby-plugin

Or

pip3 install https://github.com/lesliezhu/mkdocs-ruby-plugin/archive/refs/heads/master.zip
```

## Usage

Write kanji like this:

> 我(wo)是一只{猫(mao)}。猫(ねこ).

It will look like:

> <ruby>我<rt>wo</rt></ruby>是一只<ruby>猫<rt>mao</rt></ruby>。<ruby>猫<rt>ねこ</rt></ruby>.

Or like this when there is more than one character:

> 我(wo)是{一只猫(yizhimao)}。{綺麗猫(きれいねこ)}.

It will look like:

> <ruby>我<rt>wo</rt></ruby>是<ruby>一只猫<rt>yizhimao</rt></ruby>。<ruby>綺麗猫<rt>きれいねこ</rt></ruby>.

To enable the plugin in the `mkdocs.yml` file:

```yaml
plugins:
  - ruby:
      global_enable: true
      title_enable: true
      outer_begin: '{'
      outer_end: '}'
      inter_begin: '('
      inter_end: ')
```

If `ruby.global_enable = false`, you can enable this plugin in single page:


```markdown
---
ruby: true
---
```

If `ruby.global_enable = true`, you can disable this plugin in single page:


```markdown
---
ruby: false
---
```
