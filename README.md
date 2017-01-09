# pxtoremtool
pxtoremtool 是一款sublime 下的流式布局的网页重构计算工具
HTML5 手机端页面流式布局简易框架，配合sublime pxtoremtool 插件快速将px像素转换成rem值
# html JavaScript函数
页面加载时需要一个自执行javascript函数

  (function(doc, win) {
      var docEle = doc.documentElement,
          evt = "onorientationchange" in window ? "orientationchange" : "resize",
          fn = function() {
              var width = docEle.clientWidth;
              width && (docEle.style.fontSize = 20 * (width / 320) + "px")
          };
      win.addEventListener(evt, function() {
          setTimeout(function() {
              fn()
          }, 100)
      }, false);
      doc.addEventListener("DOMContentLoaded", fn, false)
    }(document, window));
建议在网页加载时优先执行此函数

# 插件使用

CSS中使用 “/*** + tab”键快速创建css计算公式
其中转换比例 : 640(px) 数字表示网页重构PSD宽度尺寸 不可忽略
头部其他信息均可删除

# css头部信息展示

  @charset "UTF-8";
  /*
  * Px转Rem工具
  * 转换比例 : 640(px) -> 16.0(rem)
  * 联系我们 : tools@nanweishui.com
  * 请确认您的网页渲染完毕后首先执行一下JS代码  
  * ;(function(doc,win){var docEle=doc.documentElement,evt="onorientationchange"in window?"orientationchange":"resize",fn=function(){var width=docEle.clientWidth;width&&(docEle.style.fontSize=20*(width/320)+"px")};win.addEventListener(evt,function(){setTimeout(function(){fn()},100)},false);doc.addEventListener("DOMContentLoaded",fn,false)}(document,window));
  */


css中书写的尺寸为PSD制作的真实像素尺寸，使用本插件进行快速换算（快捷键alt+x）。
