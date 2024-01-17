<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Program_Documentation</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Athlete-Performance/Statistics-Grapher-(Basketball-edition)">Athlete Performance/Statistics Grapher (Basketball edition)<a class="anchor-link" href="#Athlete-Performance/Statistics-Grapher-(Basketball-edition)">&#182;</a></h1><p>The program will first prompt the user to choose a mode, single stat display or multi stat comparison mode. Next, the program will ask the user to enter the personal data of the player (name, age, position, height, weight, and number of matches), afterwards the program will ask the user to enter the stats of the player(scores, assists, rebounds, blocks, and steals), there are two modes of entering data, the first one is single data entry wherein data to be entered must be the total data for each stat, the other mode is multi-data entry wherein the user will enter the stats for each matches played by the player. The program will then plot the data of the player in a polar graph or radar graph and display it. There is also an option where the user can compare statistical data of two to three players. The program will also display the average stats per game of the player, it is available on both single stat display mode or multi stat comparison mode.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The program has 4 modules in total including the main module.
These modules are:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="playerinfos.py">playerinfos.py<a class="anchor-link" href="#playerinfos.py">&#182;</a></h1><p>This module contains functions needed for entry and validation of a player's personal information(name, age, position, height, weight, and number matches).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!/usr/bin/env python</span>
<span class="c1"># coding: utf-8</span>

<span class="c1"># In[ ]:</span>


<span class="c1">#functions for player&#39;s personal information entry</span>
<span class="k">def</span> <span class="nf">entry_alpha</span><span class="p">(</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">loopVar</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
<span class="c1">#for entry and validation of alphabet input</span>
    <span class="c1">#for entry alphabet entry</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span><span class="nb">input</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span> <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
        <span class="c1">#for validating alphabet entry</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]:</span>
            <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">isalpha</span><span class="p">()</span><span class="o">==</span><span class="kc">True</span> <span class="ow">or</span> <span class="n">x</span><span class="o">==</span><span class="s2">&quot; &quot;</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">False</span>
            <span class="k">elif</span> <span class="n">x</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">False</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
                <span class="k">break</span>
        <span class="k">if</span> <span class="n">t</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
                <span class="k">break</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>

<span class="n">positions</span><span class="o">=</span><span class="p">[[</span><span class="s2">&quot;Point Guard&quot;</span><span class="p">,</span> <span class="s2">&quot;Shooting Guard&quot;</span><span class="p">,</span> <span class="s2">&quot;Small Forward&quot;</span><span class="p">,</span> <span class="s2">&quot;Power Forward&quot;</span><span class="p">,</span> <span class="s2">&quot;Center&quot;</span><span class="p">],</span>
          <span class="p">[</span><span class="s2">&quot;PG&quot;</span><span class="p">,</span> <span class="s2">&quot;SG&quot;</span><span class="p">,</span><span class="s2">&quot;SF&quot;</span><span class="p">,</span> <span class="s2">&quot;PF&quot;</span><span class="p">,</span> <span class="s2">&quot;C&quot;</span><span class="p">]]</span>

<span class="k">def</span> <span class="nf">position</span><span class="p">(</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">pos</span><span class="o">=</span><span class="n">positions</span><span class="p">):</span><span class="c1"># to validate or determine position of the player</span>
    <span class="c1">#If entry is more than two characters</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">])</span><span class="o">&gt;</span><span class="mi">2</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">positions</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">])</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
    <span class="c1">#If entry has a one or two characters or an acronym</span>
    <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">])</span><span class="o">&lt;=</span><span class="mi">2</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">])</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span>
        <span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">]</span><span class="o">=</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">positions</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">dictionary</span><span class="p">[</span><span class="s2">&quot;position&quot;</span><span class="p">])</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;No position exist... try again&quot;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;No position exist... try again&quot;</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">entry_numeric</span><span class="p">(</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">loopVar</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
<span class="c1">#for entry and validation of numeric input</span>
    <span class="c1">#for entry of numeric input</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span><span class="nb">input</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span> <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
        <span class="c1">#for validating numeric entry</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]:</span>
            <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
            <span class="k">if</span> <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">][</span><span class="o">-</span><span class="mi">1</span><span class="p">::]</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">()</span><span class="o">==</span><span class="kc">True</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">False</span>
            <span class="k">elif</span> <span class="n">x</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
                <span class="k">break</span>
        <span class="k">if</span> <span class="n">t</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
            <span class="k">break</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>
        
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="statentry.py">statentry.py<a class="anchor-link" href="#statentry.py">&#182;</a></h1><p>This module is comprised of functions needed for entry and validation of statistical data of the player(scores, assists, rebounds, blocks, and steals).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!/usr/bin/env python</span>
<span class="c1"># coding: utf-8</span>

<span class="c1"># In[ ]:</span>


<span class="c1">#functions for statistics entry</span>
<span class="k">def</span> <span class="nf">average</span><span class="p">(</span><span class="n">_list_</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">):</span>
    <span class="c1">#to determine the average of player based on number of matches</span>
    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">_list_</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">10</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="n">_list_</span><span class="p">)</span><span class="o">/</span><span class="n">numMatches</span>
    <span class="k">elif</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">_list_</span><span class="p">)</span><span class="o">&gt;=</span><span class="mi">10</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="n">_list_</span><span class="p">)</span><span class="o">/</span><span class="n">numMatches</span>
    
<span class="k">def</span> <span class="nf">graph_stat</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">whole</span><span class="p">):</span> 
    <span class="c1"># to compute the value needed for the graph</span>
    <span class="c1">#whole is the maximum value or the highest value for each stat derived from all-time records of the NBA</span>
    <span class="k">return</span> <span class="nb">round</span><span class="p">(</span><span class="n">part</span><span class="o">/</span><span class="n">whole</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">stat_entry</span><span class="p">(</span><span class="n">selOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
    <span class="c1"># to determine the the mode of entry</span>
    <span class="k">if</span> <span class="n">selOpt</span><span class="o">==</span><span class="s2">&quot;1&quot;</span><span class="p">:</span>
        <span class="n">single_statEntry</span><span class="p">(</span><span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">selOpt</span><span class="o">==</span><span class="s2">&quot;2&quot;</span><span class="p">:</span>
        <span class="n">multiple_statEntry</span><span class="p">(</span><span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span><span class="n">numMatches</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>
        
        
<span class="k">def</span> <span class="nf">multiple_statEntry</span><span class="p">(</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">loopVar</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
    <span class="c1"># for multi-stat entry, entering stats for each matches</span>
    <span class="n">scores</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">numMatches</span><span class="p">):</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">score</span><span class="o">=</span><span class="nb">input</span><span class="p">(</span><span class="n">prompt</span><span class="o">+</span><span class="s2">&quot;[&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">y</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">+</span><span class="s2">&quot;]: &quot;</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">score</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
                <span class="k">if</span> <span class="n">score</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">::]</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                    <span class="k">break</span>
                <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">()</span><span class="o">==</span><span class="kc">True</span><span class="p">:</span>
                    <span class="n">t</span><span class="o">=</span><span class="kc">False</span>
                <span class="k">elif</span> <span class="n">x</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
                    <span class="k">break</span>
            <span class="k">if</span> <span class="n">t</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
                <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">score</span><span class="p">))</span>
                <span class="k">break</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>
    <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span><span class="n">average</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">)</span>
            
<span class="k">def</span> <span class="nf">single_statEntry</span><span class="p">(</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">loopVar</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
    <span class="c1"># for single-entry, entering total stats based from the number of matches</span>
    <span class="n">scores</span><span class="o">=</span><span class="p">[]</span>
    <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
    <span class="k">while</span> <span class="n">t</span><span class="p">:</span>
        <span class="n">score</span><span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="n">prompt</span><span class="o">+</span><span class="s2">&quot;(Total): &quot;</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">score</span><span class="p">:</span>
            <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
            <span class="k">if</span> <span class="n">score</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">::]</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">()</span><span class="o">==</span><span class="kc">True</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">False</span>
            <span class="k">elif</span> <span class="n">x</span><span class="o">==</span><span class="s2">&quot;.&quot;</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">t</span><span class="o">=</span><span class="kc">True</span>
                <span class="k">break</span>
        <span class="k">if</span> <span class="n">t</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
            <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">score</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>
    <span class="n">dictionary</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span><span class="o">=</span> <span class="n">average</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">numMatches</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">set_val</span><span class="p">(</span><span class="n">stat</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="mf">1.0</span><span class="p">):</span>
    <span class="c1">#to set value to max if value computed is greater than the max or the limit</span>
    <span class="k">if</span> <span class="n">stat</span> <span class="o">&gt;=</span> <span class="n">limit</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">limit</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">stat</span>        
        
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="radargraph.py">radargraph.py<a class="anchor-link" href="#radargraph.py">&#182;</a></h1><p>This module contains the function to create the radar graph.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="ch">#!/usr/bin/env python</span>
<span class="c1"># coding: utf-8</span>

<span class="c1"># In[ ]:</span>


<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">matplotlib.patches</span> <span class="kn">import</span> <span class="n">Circle</span><span class="p">,</span> <span class="n">RegularPolygon</span>
<span class="kn">from</span> <span class="nn">matplotlib.path</span> <span class="kn">import</span> <span class="n">Path</span>
<span class="kn">from</span> <span class="nn">matplotlib.projections.polar</span> <span class="kn">import</span> <span class="n">PolarAxes</span>
<span class="kn">from</span> <span class="nn">matplotlib.projections</span> <span class="kn">import</span> <span class="n">register_projection</span>
<span class="kn">from</span> <span class="nn">matplotlib.spines</span> <span class="kn">import</span> <span class="n">Spine</span>
<span class="kn">from</span> <span class="nn">matplotlib.transforms</span> <span class="kn">import</span> <span class="n">Affine2D</span>


<span class="k">def</span> <span class="nf">radar_factory</span><span class="p">(</span><span class="n">num_vars</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="s1">&#39;circle&#39;</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Create a radar chart with `num_vars` axes.</span>

<span class="sd">    This function creates a RadarAxes projection and registers it.</span>

<span class="sd">    Parameters</span>
<span class="sd">    ----------</span>
<span class="sd">    num_vars : int</span>
<span class="sd">        Number of variables for radar chart.</span>
<span class="sd">    frame : {&#39;circle&#39; | &#39;polygon&#39;}</span>
<span class="sd">        Shape of frame surrounding axes.</span>

<span class="sd">    &quot;&quot;&quot;</span>
    <span class="c1"># calculate evenly-spaced axis angles</span>
    <span class="n">theta</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="p">,</span> <span class="n">num_vars</span><span class="p">,</span> <span class="n">endpoint</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">RadarAxes</span><span class="p">(</span><span class="n">PolarAxes</span><span class="p">):</span>

        <span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;radar&#39;</span>

        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="c1"># rotate plot such that the first axis is at the top</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">set_theta_zero_location</span><span class="p">(</span><span class="s1">&#39;N&#39;</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">fill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">closed</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
            <span class="sd">&quot;&quot;&quot;Override fill so that line is closed by default&quot;&quot;&quot;</span>
            <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span><span class="n">closed</span><span class="o">=</span><span class="n">closed</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">plot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
            <span class="sd">&quot;&quot;&quot;Override plot so that line is closed by default&quot;&quot;&quot;</span>
            <span class="n">lines</span> <span class="o">=</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_close_line</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">_close_line</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">line</span><span class="p">):</span>
            <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">get_data</span><span class="p">()</span>
            <span class="c1"># FIXME: markers at x[0], y[0] get doubled-up</span>
            <span class="k">if</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="n">x</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]:</span>
                <span class="n">x</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">concatenate</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="p">[</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]]))</span>
                <span class="n">y</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">concatenate</span><span class="p">((</span><span class="n">y</span><span class="p">,</span> <span class="p">[</span><span class="n">y</span><span class="p">[</span><span class="mi">0</span><span class="p">]]))</span>
                <span class="n">line</span><span class="o">.</span><span class="n">set_data</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">set_varlabels</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">labels</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">set_thetagrids</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">degrees</span><span class="p">(</span><span class="n">theta</span><span class="p">),</span> <span class="n">labels</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">_gen_axes_patch</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
            <span class="c1"># The Axes patch must be centered at (0.5, 0.5) and of radius 0.5</span>
            <span class="c1"># in axes coordinates.</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">==</span> <span class="s1">&#39;circle&#39;</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">Circle</span><span class="p">((</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">),</span> <span class="mf">0.5</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">frame</span> <span class="o">==</span> <span class="s1">&#39;polygon&#39;</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">RegularPolygon</span><span class="p">((</span><span class="o">.</span><span class="mi">5</span><span class="p">,</span> <span class="o">.</span><span class="mi">5</span><span class="p">),</span> <span class="n">num_vars</span><span class="p">,</span>
                                      <span class="n">radius</span><span class="o">=.</span><span class="mi">5</span><span class="p">,</span> <span class="n">edgecolor</span><span class="o">=</span><span class="s2">&quot;k&quot;</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;unknown value for &#39;frame&#39;: </span><span class="si">%s</span><span class="s2">&quot;</span> <span class="o">%</span> <span class="n">frame</span><span class="p">)</span>

        <span class="k">def</span> <span class="nf">draw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">renderer</span><span class="p">):</span>
            <span class="sd">&quot;&quot;&quot; Draw. If frame is polygon, make gridlines polygon-shaped &quot;&quot;&quot;</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">==</span> <span class="s1">&#39;polygon&#39;</span><span class="p">:</span>
                <span class="n">gridlines</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">yaxis</span><span class="o">.</span><span class="n">get_gridlines</span><span class="p">()</span>
                <span class="k">for</span> <span class="n">gl</span> <span class="ow">in</span> <span class="n">gridlines</span><span class="p">:</span>
                    <span class="n">gl</span><span class="o">.</span><span class="n">get_path</span><span class="p">()</span><span class="o">.</span><span class="n">_interpolation_steps</span> <span class="o">=</span> <span class="n">num_vars</span>
            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">draw</span><span class="p">(</span><span class="n">renderer</span><span class="p">)</span>


        <span class="k">def</span> <span class="nf">_gen_axes_spines</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">==</span> <span class="s1">&#39;circle&#39;</span><span class="p">:</span>
                <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">_gen_axes_spines</span><span class="p">()</span>
            <span class="k">elif</span> <span class="n">frame</span> <span class="o">==</span> <span class="s1">&#39;polygon&#39;</span><span class="p">:</span>
                <span class="c1"># spine_type must be &#39;left&#39;/&#39;right&#39;/&#39;top&#39;/&#39;bottom&#39;/&#39;circle&#39;.</span>
                <span class="n">spine</span> <span class="o">=</span> <span class="n">Spine</span><span class="p">(</span><span class="n">axes</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span>
                              <span class="n">spine_type</span><span class="o">=</span><span class="s1">&#39;circle&#39;</span><span class="p">,</span>
                              <span class="n">path</span><span class="o">=</span><span class="n">Path</span><span class="o">.</span><span class="n">unit_regular_polygon</span><span class="p">(</span><span class="n">num_vars</span><span class="p">))</span>
                <span class="c1"># unit_regular_polygon gives a polygon of radius 1 centered at</span>
                <span class="c1"># (0, 0) but we want a polygon of radius 0.5 centered at (0.5,</span>
                <span class="c1"># 0.5) in axes coordinates.</span>
                <span class="n">spine</span><span class="o">.</span><span class="n">set_transform</span><span class="p">(</span><span class="n">Affine2D</span><span class="p">()</span><span class="o">.</span><span class="n">scale</span><span class="p">(</span><span class="o">.</span><span class="mi">5</span><span class="p">)</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="o">.</span><span class="mi">5</span><span class="p">,</span> <span class="o">.</span><span class="mi">5</span><span class="p">)</span>
                                    <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">transAxes</span><span class="p">)</span>
                


                <span class="k">return</span> <span class="p">{</span><span class="s1">&#39;polar&#39;</span><span class="p">:</span> <span class="n">spine</span><span class="p">}</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;unknown value for &#39;frame&#39;: </span><span class="si">%s</span><span class="s2">&quot;</span> <span class="o">%</span> <span class="n">frame</span><span class="p">)</span>

    <span class="n">register_projection</span><span class="p">(</span><span class="n">RadarAxes</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">theta</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Main.py">Main.py<a class="anchor-link" href="#Main.py">&#182;</a></h1><p>This module is the main module of the program.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The main module imports the following modules and functions:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">playerinfos</span> <span class="kn">import</span> <span class="n">entry_alpha</span><span class="p">,</span> <span class="n">entry_numeric</span><span class="p">,</span> <span class="n">position</span>
<span class="kn">from</span> <span class="nn">statentry</span> <span class="kn">import</span> <span class="n">graph_stat</span><span class="p">,</span> <span class="n">stat_entry</span><span class="p">,</span> <span class="n">set_val</span>
<span class="kn">from</span> <span class="nn">radargraph</span> <span class="kn">import</span> <span class="n">radar_factory</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The first code of the program will prompt the user to select a mode by typing "single" or "multi". If the user choose "single", the program will only ask information and data on one player. If the user chooses "multi", the program will ask the user to enter the number of players, with maximum limit of entry, the user will also be asked for  information and statistis of multiple players.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Welcome to the Athlete Performance Grapher!&quot;</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Choose: Type </span><span class="se">\&quot;</span><span class="s2">single</span><span class="se">\&quot;</span><span class="s2"> for single stat display mode and Type </span><span class="se">\&quot;</span><span class="s2">multi</span><span class="se">\&quot;</span><span class="s2"> for stat comparison mode.&quot;</span><span class="p">)</span>
    <span class="n">mode</span><span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Type mode: &quot;</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">mode</span> <span class="o">==</span> <span class="s2">&quot;multi&quot;</span> <span class="ow">or</span> <span class="n">mode</span> <span class="o">==</span> <span class="s2">&quot;single&quot;</span><span class="p">:</span>
        <span class="k">break</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry.&quot;</span><span class="p">)</span>
        <span class="k">continue</span>
        
<span class="k">if</span> <span class="n">mode</span><span class="o">==</span><span class="s2">&quot;single&quot;</span><span class="p">:</span>
    <span class="n">num</span><span class="o">=</span><span class="mi">1</span>
    
<span class="k">else</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">num</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Enter number of players to be compared(max is 3): &quot;</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">num</span><span class="o">==</span><span class="mi">3</span> <span class="ow">or</span> <span class="n">num</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span>
            <span class="k">break</span>            
        <span class="k">elif</span> <span class="n">num</span><span class="o">&gt;</span><span class="mi">3</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Exceeded maximum entry, Input a lower number&quot;</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Enter a number higher than zero.&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This part of the code will ask the user to enter the personal information of the player/s, the three variables below(data, playerInfos, playerStats) will be appended with values in the later part of the program. The set of codes for entering personal information is loop within a range that depends on the mode, if single, it will automatically set num to 1 in able to get informations from only one player and if it is multi, the program will ask the user to enter personal information  of multiple players. The personal informations that will be entered by the user will be stored in a dictionary with identifier=infos.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="p">[[</span><span class="s2">&quot;Scoring&quot;</span><span class="p">,</span> <span class="s2">&quot;Assisting&quot;</span><span class="p">,</span> <span class="s2">&quot;Rebounding&quot;</span><span class="p">,</span> <span class="s2">&quot;Blocking&quot;</span><span class="p">,</span> <span class="s2">&quot;Stealing&quot;</span><span class="p">],</span>
        <span class="p">(</span><span class="s1">&#39;Player Stats&#39;</span><span class="p">,</span> <span class="p">[])]</span>

<span class="n">playerInfos</span><span class="o">=</span><span class="p">[]</span>
<span class="n">playerStats</span><span class="o">=</span><span class="p">[]</span>

<span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">x</span><span class="o">&gt;=</span><span class="mi">1</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Next Player: &quot;</span><span class="p">)</span>
    <span class="n">infos</span><span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">,</span><span class="s2">&quot;position&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s2">&quot;height&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s2">&quot;weight&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s2">&quot;matches&quot;</span><span class="p">:</span><span class="s1">&#39;&#39;</span><span class="p">}</span>
    <span class="n">playerInfos</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">infos</span><span class="p">)</span>
    <span class="c1">#to enter player&#39;s personal information</span>
    <span class="k">for</span> <span class="n">info</span> <span class="ow">in</span> <span class="n">infos</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;name&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the name of the player: &quot;</span>
            <span class="n">entry_alpha</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;age&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the age of the player: &quot;</span>
            <span class="n">entry_numeric</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;position&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the main position played by the player: &quot;</span>
            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">entry_alpha</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
                <span class="n">t</span><span class="o">=</span><span class="n">position</span><span class="p">(</span><span class="n">infos</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">t</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
                    <span class="k">break</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">continue</span>
        <span class="k">elif</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;height&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the height of the player(cm): &quot;</span>
            <span class="n">entry_numeric</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;weight&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the weight of the player(kg): &quot;</span>
            <span class="n">entry_numeric</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">info</span><span class="o">==</span><span class="s2">&quot;matches&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter the number of matches played: &quot;</span>
            <span class="n">entry_numeric</span><span class="p">(</span><span class="n">infos</span><span class="p">,</span> <span class="n">info</span><span class="p">,</span> <span class="n">prompt</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This part of the code  is the code for entering, validating, computing, and storing statistical data from the user. Similar to the codes above, these codes will ask data depending on the mode. The user will first be prompted to enter a mode of data entry which is entry Total by typing "1" or entry multiple data by typing "2". In entry total the user will only be asked the total stats of the player on all the games, on the other hand, in entry multiple data, the user will be asked to enter stats on each of their matches one by one. After entry of statistical data, the program will automatically average the inputs, these average will be stored in the aveStats dictionary. In computing average of the stats, the entered data for each stat will totaled before divided by number of matches if entry multiple data is selected, otherwise (entry Total) the inputs will be divided  by the player's number of matches, this will later be displayed at the later part of the code. The program will also compute the value of the stats that will be used in making the plot or the graph. In computing this "graph stat", the average stats will be rated by dividing it by the maxValues or the max/limit of the stat possible(based from all-time records of the NBA). After computations, the aveStats will be appended to playerStats list and the statistics will be appended on data[1][1] list.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">aveStats</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;Scoring&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Assisting&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Rebounding&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span><span class="s2">&quot;Blocking&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Stealing&quot;</span><span class="p">:</span><span class="mi">0</span><span class="p">}</span>


    <span class="c1">#Values for max_value in def graph_stat</span>
    <span class="n">maxValues</span><span class="o">=</span><span class="p">[</span><span class="mf">30.12</span><span class="p">,</span> <span class="mf">11.19</span><span class="p">,</span> <span class="mf">22.89</span><span class="p">,</span> <span class="mf">3.50</span><span class="p">,</span> <span class="mf">2.71</span><span class="p">]</span>

    <span class="c1">#to enter player&#39;s statistical data</span>
    <span class="k">for</span> <span class="n">stat</span> <span class="ow">in</span> <span class="n">aveStats</span><span class="p">:</span>
        <span class="k">while</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Scoring&quot;</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Select input option: entry Total or entry multiple data&quot;</span><span class="p">)</span>
            <span class="n">selectedOpt</span><span class="o">=</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Type 1 for entry total, 2 for multiple entry: &quot;</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">selectedOpt</span><span class="o">==</span><span class="s2">&quot;1&quot;</span> <span class="ow">or</span> <span class="n">selectedOpt</span><span class="o">==</span><span class="s2">&quot;2&quot;</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid entry, Try again&quot;</span><span class="p">)</span>

        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">()</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">stat</span><span class="p">,</span> <span class="s2">&quot;Statistic:&quot;</span><span class="p">)</span>
            <span class="k">break</span>        
        <span class="k">if</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Scoring&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter Score&quot;</span>
            <span class="n">stat_entry</span><span class="p">(</span><span class="n">selectedOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">infos</span><span class="p">[</span><span class="s2">&quot;matches&quot;</span><span class="p">]),</span> <span class="n">prompt</span><span class="p">)</span>
            <span class="n">scoring</span><span class="o">=</span><span class="nb">round</span><span class="p">(</span><span class="n">graph_stat</span><span class="p">(</span><span class="n">aveStats</span><span class="p">[</span><span class="n">stat</span><span class="p">],</span><span class="n">maxValues</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">),</span><span class="mi">2</span><span class="p">)</span>
            <span class="n">scoring</span><span class="o">=</span><span class="n">set_val</span><span class="p">(</span><span class="n">scoring</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Assisting&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter Assists&quot;</span>
            <span class="n">stat_entry</span><span class="p">(</span><span class="n">selectedOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">infos</span><span class="p">[</span><span class="s2">&quot;matches&quot;</span><span class="p">]),</span> <span class="n">prompt</span><span class="p">)</span>
            <span class="n">assisting</span><span class="o">=</span><span class="nb">round</span><span class="p">(</span><span class="n">graph_stat</span><span class="p">(</span><span class="n">aveStats</span><span class="p">[</span><span class="n">stat</span><span class="p">],</span> <span class="n">maxValues</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span><span class="mi">2</span><span class="p">)</span>
            <span class="n">assisting</span><span class="o">=</span><span class="n">set_val</span><span class="p">(</span><span class="n">assisting</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Rebounding&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter Rebounds&quot;</span>
            <span class="n">stat_entry</span><span class="p">(</span><span class="n">selectedOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">infos</span><span class="p">[</span><span class="s2">&quot;matches&quot;</span><span class="p">]),</span> <span class="n">prompt</span><span class="p">)</span>
            <span class="n">rebounding</span><span class="o">=</span><span class="nb">round</span><span class="p">(</span><span class="n">graph_stat</span><span class="p">(</span><span class="n">aveStats</span><span class="p">[</span><span class="n">stat</span><span class="p">],</span> <span class="n">maxValues</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span> <span class="mi">2</span><span class="p">)</span>
            <span class="n">rebounding</span><span class="o">=</span><span class="n">set_val</span><span class="p">(</span><span class="n">rebounding</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Blocking&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter Blocks&quot;</span>
            <span class="n">stat_entry</span><span class="p">(</span><span class="n">selectedOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">infos</span><span class="p">[</span><span class="s2">&quot;matches&quot;</span><span class="p">]),</span> <span class="n">prompt</span><span class="p">)</span>
            <span class="n">blocking</span><span class="o">=</span><span class="nb">round</span><span class="p">(</span><span class="n">graph_stat</span><span class="p">(</span><span class="n">aveStats</span><span class="p">[</span><span class="n">stat</span><span class="p">],</span> <span class="n">maxValues</span><span class="p">[</span><span class="mi">3</span><span class="p">]),</span> <span class="mi">2</span><span class="p">)</span>
            <span class="n">blocking</span><span class="o">=</span><span class="n">set_val</span><span class="p">(</span><span class="n">blocking</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">stat</span><span class="o">==</span><span class="s2">&quot;Stealing&quot;</span><span class="p">:</span>
            <span class="n">prompt</span><span class="o">=</span><span class="s2">&quot;Enter Steals&quot;</span>
            <span class="n">stat_entry</span><span class="p">(</span><span class="n">selectedOpt</span><span class="p">,</span> <span class="n">aveStats</span><span class="p">,</span> <span class="n">stat</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">infos</span><span class="p">[</span><span class="s2">&quot;matches&quot;</span><span class="p">]),</span> <span class="n">prompt</span><span class="p">)</span>
            <span class="n">stealing</span><span class="o">=</span><span class="n">set_val</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">graph_stat</span><span class="p">(</span><span class="n">aveStats</span><span class="p">[</span><span class="n">stat</span><span class="p">],</span> <span class="n">maxValues</span><span class="p">[</span><span class="mi">4</span><span class="p">]),</span> <span class="mi">2</span><span class="p">))</span>
            <span class="n">stealing</span><span class="o">=</span> <span class="n">set_val</span><span class="p">(</span><span class="n">stealing</span><span class="p">)</span>
    <span class="n">playerStats</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">aveStats</span><span class="p">)</span>        
    <span class="n">statistics</span><span class="o">=</span><span class="p">[</span><span class="n">scoring</span><span class="p">,</span> <span class="n">assisting</span><span class="p">,</span> <span class="n">rebounding</span><span class="p">,</span> <span class="n">blocking</span><span class="p">,</span> <span class="n">stealing</span><span class="p">]</span>
    <span class="n">data</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">statistics</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This part of code is the code for making the radar graph, here N's value was set depending on the number of stats evaluated, in this program's case, it is five ("Scoring", "Assisting", "Rebounding", "Blocking", "Stealing") from index 0 of data variable that was mentioned earlier. This value will be used as a parameter for radar_factory. theta is the variable that will be used to create the plot, including its axes, and the frame which is polygon-shaped. spoke_labels is from the return value of data.pop(0), removing the index zero of data. The remaining values from within the tuple of data is set as title, and stat_data respectively. fig was set as the variable for the figure of the program and ax is for the subplot. It is also adjusted with the values below and has a set limit for yaxis=1.0. Here, the label for each grid was also set as well as the title within the subplot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#for making the radar graph</span>
<span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">theta</span> <span class="o">=</span> <span class="n">radar_factory</span><span class="p">(</span><span class="n">N</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="s1">&#39;polygon&#39;</span><span class="p">)</span>

<span class="n">spoke_labels</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="n">title</span><span class="p">,</span> <span class="n">stat_data</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

<span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">6</span><span class="p">),</span> <span class="n">subplot_kw</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">projection</span><span class="o">=</span><span class="s1">&#39;radar&#39;</span><span class="p">))</span>
<span class="n">fig</span><span class="o">.</span><span class="n">subplots_adjust</span><span class="p">(</span><span class="n">top</span><span class="o">=</span><span class="mf">0.85</span><span class="p">,</span> <span class="n">bottom</span><span class="o">=</span><span class="mf">0.05</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mf">1.0</span><span class="p">)</span>

<span class="n">ax</span><span class="o">.</span><span class="n">set_rgrids</span><span class="p">([</span><span class="mf">0.2</span><span class="p">,</span> <span class="mf">0.4</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">])</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">title</span><span class="p">,</span>  <span class="n">position</span><span class="o">=</span><span class="p">(</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">1.1</span><span class="p">),</span> <span class="n">ha</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This part of the code is for drawing the lines, its fill, and its points depending on the data. The colors list have elements that is used as parameters by the other codes to display the corresponding color. Here, to create a the lines, line was set as a variable that modifies the subplot. fill is used to fill the gap made by the lines and scatter to put points on the subplot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">,</span> <span class="s1">&#39;m&#39;</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]</span>


<span class="k">for</span> <span class="n">d</span><span class="p">,</span> <span class="n">color</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">stat_data</span><span class="p">,</span><span class="n">colors</span><span class="p">):</span>
    <span class="n">line</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">theta</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span><span class="n">theta</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span>  <span class="n">alpha</span><span class="o">=</span><span class="mf">0.25</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">theta</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This set of codes is composed of a function that searches and gets the name of the players inputted if the mode is multi. These names are then used to dispaly legends on the graph with their corresponding color.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">legend_name</span><span class="p">(</span><span class="n">playerInfos</span><span class="o">=</span><span class="n">playerInfos</span><span class="p">):</span>
    <span class="c1">#for getting first name for legends in multi mode</span>
    <span class="n">names</span><span class="o">=</span><span class="p">[]</span> 
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">playerInfos</span><span class="p">)):</span>
        <span class="n">firstName</span><span class="o">=</span> <span class="n">playerInfos</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
        <span class="n">names</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">firstName</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">names</span>
        
<span class="n">names</span><span class="o">=</span><span class="n">legend_name</span><span class="p">()</span>

<span class="k">if</span>  <span class="n">mode</span><span class="o">==</span><span class="s2">&quot;multi&quot;</span><span class="p">:</span>   
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">names</span><span class="p">)</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span>
        <span class="n">labels</span> <span class="o">=</span> <span class="p">(</span><span class="n">names</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">names</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">names</span><span class="p">)</span><span class="o">==</span><span class="mi">3</span><span class="p">:</span>
        <span class="n">labels</span><span class="o">=</span><span class="p">(</span><span class="n">names</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">names</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">names</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
    <span class="n">legend</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">labels</span><span class="p">,</span> <span class="n">loc</span><span class="o">=</span><span class="p">(</span><span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.95</span><span class="p">),</span>
                        <span class="n">labelspacing</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="s1">&#39;medium&#39;</span><span class="p">)</span>
    
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a function for getting the personal information and the stats of the player that will be displayed on the plot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#to get personal info and stats of the player to be displayed</span>
<span class="k">def</span> <span class="nf">get_infoStats</span><span class="p">(</span><span class="n">playerStats</span><span class="p">,</span> <span class="n">playerInfos</span><span class="p">):</span>
        <span class="n">line1</span><span class="o">=</span> <span class="s2">&quot;Name: &quot;</span><span class="o">+</span> <span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span><span class="o">+</span><span class="s2">&quot;     &quot;</span><span class="o">+</span><span class="s2">&quot;age: &quot;</span><span class="o">+</span> <span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;age&quot;</span><span class="p">)</span>
        <span class="n">line2</span><span class="o">=</span> <span class="s2">&quot;Position: &quot;</span><span class="o">+</span> <span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;position&quot;</span><span class="p">)</span>
        <span class="n">line3</span><span class="o">=</span> <span class="s2">&quot;Height: &quot;</span><span class="o">+</span> <span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;height&quot;</span><span class="p">)</span><span class="o">+</span><span class="s2">&quot;cm&quot;</span><span class="o">+</span><span class="s2">&quot;     &quot;</span><span class="o">+</span><span class="s2">&quot;Weight: &quot;</span><span class="o">+</span><span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;weight&quot;</span><span class="p">)</span><span class="o">+</span><span class="s2">&quot;kg&quot;</span>
        <span class="n">line4</span><span class="o">=</span> <span class="s2">&quot;Matches: &quot;</span><span class="o">+</span> <span class="n">playerInfos</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;matches&quot;</span><span class="p">)</span>
        <span class="n">lines1</span><span class="o">=</span><span class="p">[</span><span class="n">line1</span><span class="p">,</span> <span class="n">line2</span><span class="p">,</span> <span class="n">line3</span><span class="p">,</span> <span class="n">line4</span><span class="p">]</span>

        <span class="n">line5</span><span class="o">=</span> <span class="s2">&quot;Scores per game: &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">playerStats</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;Scoring&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">line6</span><span class="o">=</span> <span class="s2">&quot;Assists per game: &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">playerStats</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;Assisting&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">line7</span><span class="o">=</span> <span class="s2">&quot;Rebounds per game: &quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">playerStats</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;Rebounding&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">line8</span><span class="o">=</span> <span class="s2">&quot;Blocking per game: &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">playerStats</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;Blocking&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">line9</span><span class="o">=</span> <span class="s2">&quot;Steals per game: &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">playerStats</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;Stealing&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">))</span>
        <span class="n">lines2</span><span class="o">=</span><span class="p">[</span><span class="n">line5</span><span class="p">,</span> <span class="n">line6</span><span class="p">,</span> <span class="n">line7</span><span class="p">,</span> <span class="n">line8</span><span class="p">,</span> <span class="n">line9</span><span class="p">]</span>
        
        <span class="k">return</span> <span class="n">lines1</span><span class="p">,</span> <span class="n">lines2</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a function for placing and displaying the collected information within the plot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#to display the personal info and stats of the player within the plot</span>
<span class="k">def</span> <span class="nf">place_infoStats</span><span class="p">(</span><span class="n">lines1</span><span class="p">,</span> <span class="n">lines2</span><span class="p">,</span> <span class="n">points</span><span class="p">,</span> <span class="n">loopVar</span><span class="p">,</span>  <span class="n">xaxis1</span><span class="o">=</span><span class="mf">1.0</span><span class="p">,</span> <span class="n">xaxis2</span><span class="o">=</span><span class="mf">1.5</span><span class="p">,</span> <span class="n">num</span><span class="o">=</span><span class="n">num</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">num</span><span class="o">&gt;</span><span class="mi">1</span><span class="p">:</span>
        <span class="n">x</span><span class="o">=</span><span class="n">xaxis2</span> 
    <span class="k">else</span><span class="p">:</span>
        <span class="n">x</span><span class="o">=</span><span class="n">xaxis1</span>
    <span class="k">if</span> <span class="n">e</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span>
        <span class="n">f</span><span class="o">=</span><span class="n">points</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">f</span><span class="o">=</span><span class="mf">0.90</span>
        
    <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">4</span><span class="p">):</span>
        <span class="n">fig</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">xaxis1</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">lines1</span><span class="p">[</span><span class="n">c</span><span class="p">],</span>
                 <span class="n">horizontalalignment</span><span class="o">=</span><span class="s1">&#39;left&#39;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">weight</span><span class="o">=</span><span class="s1">&#39;medium&#39;</span><span class="p">,</span>
                 <span class="n">size</span><span class="o">=</span><span class="s1">&#39;large&#39;</span><span class="p">)</span>
        <span class="n">f</span><span class="o">-=</span><span class="mf">0.04</span>
    <span class="k">if</span> <span class="n">num</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
        <span class="n">g</span><span class="o">=</span><span class="mf">0.60</span>
    <span class="k">elif</span> <span class="n">e</span><span class="o">&gt;=</span><span class="mi">0</span><span class="p">:</span>
        <span class="n">g</span><span class="o">=</span><span class="n">points</span><span class="p">[</span><span class="n">loopVar</span><span class="p">]</span>
        
    <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
        <span class="n">fig</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">g</span><span class="p">,</span> <span class="n">lines2</span><span class="p">[</span><span class="n">b</span><span class="p">],</span>
                <span class="n">horizontalalignment</span><span class="o">=</span><span class="s1">&#39;left&#39;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">weight</span><span class="o">=</span><span class="s1">&#39;medium&#39;</span><span class="p">,</span>
                <span class="n">size</span><span class="o">=</span><span class="s1">&#39;large&#39;</span><span class="p">)</span>
        <span class="n">g</span><span class="o">-=</span><span class="mf">0.04</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Here are the last set of codes. The first line of code is used to display the labels in the graph in their corresponding angles of designation. plt.show() is used to display the graph or the plot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ax</span><span class="o">.</span><span class="n">set_varlabels</span><span class="p">(</span><span class="n">spoke_labels</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Here-is-a-sample-output-of-multi-stat-comparison-mode:">Here is a sample output of multi stat comparison mode:<a class="anchor-link" href="#Here-is-a-sample-output-of-multi-stat-comparison-mode:">&#182;</a></h1><p><img src="data:image/png;base64,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UUIIlyJciRlyiEVHiAvHwEAwEH4YYRvkhWTY1emSvhZlDpREGNQe4Y2gLsK0CIva3IbxQdgVRgtCiEm2sRwVbuRRGY7wkyeEAcOIbmmkRLXemMBOJZDPNI0gTPG+8DqWz3ijPkVuFnkbaaCXYVfMdnW+JLwaKXmtRsYHOSKEXXFthFyQ0kiJ3d6YgAmYgAmYgAmYwPgJpGKSNTHd7vER/01uB2EcyyR9NApgfJzXIOGcY9WEcwwXlBnCSr4TCa+tPB9lwvmHR2l80Mx3FgnnKGEktVtMoJcIZLgjIY30sddE40rjg1yqen0Ko+Pz0S85971xLp4PjA/6HJM/5CQM2ccbGR+cTu4V+ScknFM3fdZiAiZgAiZgAiZgAibQBgFyVhCUNIwpQrEsJmACjQlkn8FwIXTrA42L+ogJmIAJmIAJmIAJmEBJgGlIGVFmJJdpQ1GoLCZgAo0JYGzQZ/By4vXYq3FRHzEBEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABEzABE5g6BP4P4Xf5x0I8R+EAAAAASUVORK5CYII=" alt="image.png"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Here-is-a-sample-output-for-single-stat-display-mode:">Here is a sample output for single stat display mode:<a class="anchor-link" href="#Here-is-a-sample-output-for-single-stat-display-mode:">&#182;</a></h1><p><img src="data:image/png;base64,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Cm6rEQKGNGFIR4rIFP0uuH/j6d4pkLNTUjwLCBq00ZcmnTN9gaCVuc69JCJ/0O+vMbHi9NkkaC6U+JEIEAEiUCQEzOQNTRRIFQgNSNHCNOMBQbvSdQ4E7UBtoklF0LAAGLMpbsNf924Tp2kKgQdoGwKCZrQDmQiaWzNmTKfdSdA0itxUZwTMe2fGuEhE2moNGAJ2IDB7pnqnYNo/WV/j3oCg4V17z/WHD86bvvDe4T0xgvcHf+gc5PKBwzkSNIMQt0SACBCBIiJgJm8MARM1TJMwDSLyC74xEPipgIRBQKK+0SYS+KkZE+ftIvKGvqaLiMDk2FBrtdAWTKIwQa7yQNBg4gSxg8CcY8bo1i6k08zFtKlnF03yoBlwEzndLDdEoKgImN80BgGXgKVae+3+jad7p+ArCj8y80eM28TZWkSeExFox4yYvtIRNPiswcSJviHwTXMTOX2YGyJABIgAEbCJgJm8TZ9ItfFH7Y8CXzOYTKaKyD/0BSBoz6QJEsC55CABkDtM+DDhfKSdlLNp0NxBAnfkSNAwzGtdQQJYqBCIQCEC1QkB41oAFwK8Y2fowbkJGnw7U71TIGZP6/cS996s74UGDQQN7xwCdkzgjHnH0xE03A5fUPjDIUgAbeOdpRABIkAEiAAR8BUB+NBBsJCBcMLsSSECRCA9AuadAbmDmfQv6S/lGSJABIgAESAC+SGAFATQTEAjgJQBWHQoRIAIpEcAhAzvDLTl0J41Tn8pzxABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgGiYEdAAABCElEQVQQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABGoLgj8f2bjxBoMdizpAAAAAElFTkSuQmCC" alt="image.png"></p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
