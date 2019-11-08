(function(){Bootstrap.GrowlNotifications=Ember.CollectionView.extend({classNames:["growl-notifications"],contentBinding:"Bootstrap.GNM.notifications",attributeBindings:["style"],showTime:1e4,unitHeight:80,unitWidth:320,itemViewClass:Ember.View.extend({classNames:["growl-notification"],template:Ember.Handlebars.compile('<span class="icon"><i class="fa {{unbound view.iconType}}"></i></span>\n<a class="close-notification" {{action "close" target="view"}}>\n    <span style="font-size: 15px;"><i class="fa fa-times"></i></span>\n</a>\n<strong>\n    {{view.content.title}}\n</strong>\n<p>\n    {{view.content.sub}}\n</p>'),classNameBindings:[":growl-notification","content.closed","isOpaque"],attributeBindings:["style"],timeoutId:null,isOpaque:false,init:function(){var t,e=this;this._super();t=function(){return e.notifyPropertyChange("style")};this.set("_recomputeStyle",t);return $(window).bind("resize",t)},didInsertElement:function(){var t=this;this.set("timeoutId",setTimeout(function(){return t.send("close")},this.get("parentView.showTime")));return Ember.run.later(this,function(){return this.set("isOpaque",true)},1)},willDestroyElement:function(){return $(window).unbind("resize",this.get("_recomputeStyle"))},style:function(){var t,e,n,i,o,s,r,a,c,l;n=this.get("parentView.content").rejectProperty("closed",true);e=n.indexOf(this.get("content"));l=$(window).height();r=this.get("parentView.unitHeight");a=this.get("parentView.unitWidth");c=Math.floor(l/r);t=Math.floor(e/c);o=e%c;if(e===-1){return""}s=o*r;i=t*a;return"top: "+s+"px; right: "+i+"px;"}.property("parentView.content.@each.closed"),iconType:function(){var t,e;e=this.get("content.type");t={info:"fa-bullhorn",success:"fa-check",warning:"fa-exclamation",danger:"fa-times"};return t[e]||""}.property("content.type"),actions:{close:function(){var t=this;this.set("isOpaque",false);return setTimeout(function(){t.get("parentView.content").removeObject(t.get("content"));return clearTimeout(t.get("timeoutId"))},300)}}})});Ember.Handlebars.helper("bs-growl-notifications",Bootstrap.GrowlNotifications);Bootstrap.GNM=Bootstrap.GrowlNotificationManager=Ember.Object.create({notifications:Ember.A(),push:function(t,e,n){var i;n=n!=null?n:n="info";i=Bootstrap.Notification.create({title:t,sub:e,type:n,closed:false});return this.get("notifications").pushObject(i)}});Bootstrap.GrowlNotification=Ember.Object.extend()}).call(this);