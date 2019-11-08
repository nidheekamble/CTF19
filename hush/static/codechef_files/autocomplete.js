(function(){Ember.TEMPLATES["defaultItemContainer"]=Ember.Handlebars.compile("{{text}}");Ember.TEMPLATES["components/auto-complete"]=Ember.Handlebars.compile("<div id='cc-auto' {{bind-attr class=cssclass}} >{{view textField placeholder=placeholder class=cssclass size=size maxlength=maxlength valueBinding='searchText'}}{{#if ulVisible}}{{view UlView contextBinding='searchResults' index=currentIndex}}{{/if}}</div>");Ember.TEMPLATES["ulViewContainer"]=Ember.Handlebars.compile("{{#each item in this}}{{view view.parentView.ItemView contextBinding='item' currentIndex=view.parentView.currentIndex}}{{/each}}");var e=Ember.Component.extend({cache:Ember.Map.create(),listItemContainer:"defaultItemContainer",isAutoCompleteOn:true,localdata:[],isValid:false,ulVisible:true,primaryText:"text",minLength:3,listLimit:7,url:"",searchText:null,searchObj:null,currentIndex:-1,qParam:null,propertiesToSearch:null,getPropertiesToSearch:function(){return!Ember.isEmpty(this.get("propertiesToSearch"))?this.get("propertiesToSearch").split(","):Ember.A([this.get("primaryText")])}.property("propertiesToSearch"),searchResults:[],value:"",valueType:"text",populateResults:true,lastAutoCompleteCallTimer:null,ajax:function(e){var t=this;return $.ajax({dataType:e["dataType"]?e["dataType"]:"JSON",url:e["url"],type:e["type"]?e["type"]:"GET",data:e["data"],retryCount:e["retryCount"]?e["retryCount"]:0,retryLimit:10,success:function(t){if(typeof e["success"]=="function"){e["success"](t)}},error:function(s){if(s.status>=499&&this.retryCount<this.retryLimit){e["retryCount"]=e["retryCount"]?e["retryCount"]+1:1;setTimeout(function(){t.ajax(e)},2e3)}else{if(typeof e["error"]=="function"){e["error"](s)}}}})},focusOut:function(e){if(this.get("ulVisible")){this.send("focusOut",e)}},keyDown:function(e){if(e.keyCode==9){this.send("changeText")}else{this.send("traverse",e)}},click:function(e){this.send("changeText",this.get("currentIndex"))},mouseEnter:function(e){this.send("changeMouseState",true)},mouseLeave:function(e){this.send("changeMouseState",false)},textField:Ember.TextField.extend({enter:"changeText"}),ItemView:Ember.View.extend(Ember.ViewTargetActionSupport,{classNameBindings:["staticClass","dynamicClass"],staticClass:"cc-menu-item",dynamicClass:function(){return this.get("context").get("internal_id")==this.get("currentIndex")?"is-active":""}.property("currentIndex"),tagName:"li",templateNameBinding:"getTemplate",getTemplate:function(){return this.get("targetObject").get("listItemContainer")}.property(),mouseEnter:function(e){this.triggerAction({action:"setCurrentIndex",actionContext:this.get("context").get("internal_id")})}}),UlView:Ember.View.extend({tagName:"ul",classNameBindings:["staticClass","dynamicClass"],staticClass:"cc-autocomplete",templateName:"ulViewContainer",dynamicClass:function(){return this.get("context").length==0?"none":""}.property("context"),didInsertElement:function(){var e=$(this.get("parentView").$()).find("[type=text]").outerWidth();this.$().css("min-width",e)}}),IsNumeric:function(e){return e>=0||e<0},getFilteredData:function(e){var t;var s=this;t=$.grep(e,function(e,t){e=Ember.Object.create(e);var i=0;$.each(s.get("getPropertiesToSearch"),function(t,r){var a=r.trim();i=i||e.get(a).toString().toLowerCase().indexOf(s.get("searchText").toLowerCase())+1});return i>0});return t.toArray()},getAutocompleteURL:function(){var e=this.get("searchText");var t=this.get("url");return this.get("qParam")==null?t+e:t+"?"+this.get("qParam")+"="+e},searchTextObserver:function(){if(!this.get("isAutoCompleteOn")){return}if(!this.get("populateResults")){return}var e=this;var t=this.get("searchText");if(!Ember.isEmpty(t)&&t.length<this.get("minLength")){this.set("searchResults",[])}else if(!Ember.isEmpty(t)&&t.length>=this.get("minLength")){var s=[];var i=this.get("url");if(Ember.isEmpty(this.get("localdata"))){var r=this.getAutocompleteURL();s=this.get("cache").get(r);if(Ember.isEmpty(s)){e.scheduleFetchDataCall()}else{e.setSearchResults(e.prepareSearchResults(s,e));e.validateSearchText()}}else{s=this.getFilteredData(this.get("localdata"));e.setSearchResults(e.prepareSearchResults(s,e));e.validateSearchText()}}}.observes("searchText"),prepareSearchResults:function(e,t){var s=t;var i=Ember.A();$.each(e,function(e,t){if(typeof t=="string"){i.pushObject(Ember.Object.create({internal_id:e,text:t}))}else if(typeof t=="object"){var r=Ember.Object.create(t);r.set("internal_id",e);r.set("text",r.get(s.get("primaryText")));i.pushObject(r)}});return i},scheduleFetchDataCall:function(){var e=this;var t=this.get("lastAutoCompleteCallTimer");if(!Ember.isEmpty(t)){clearTimeout(t)}var s=function(){var t=e.getAutocompleteURL();e.ajax({type:"GET",url:t,async:true,dataType:"JSON",success:function(s){e.get("cache").set(t,s);e.setSearchResults(e.prepareSearchResults(s,e));e.validateSearchText()}})};t=setTimeout(s,500);this.set("lastAutoCompleteCallTimer",t)},setSearchResults:function(e){var t=this.get("listLimit");this.set("searchResults",e.splice(0,t))},actions:{changeText:function(e){if(!this.IsNumeric(e)){e=this.get("currentIndex")}if(e==-1)return;if(this.get("searchResults").length==0){this.set("enterEvent",true);return}var t=this.get("searchResults").filterBy("internal_id",e).get(0);this.set("populateResults",false);this.set("searchText",t.get(this.get("primaryText")));this.set("searchObj",t);this.set("value",t.get(this.get("valueType")));this.validateSearchText();this.set("searchResults",Ember.A());this.set("populateResults",true);this.set("enterEvent",false)},traverse:function(e){var t=e.keyCode;var s=this.get("currentIndex");switch(t){case 40:s++;s=Math.min(s,this.get("searchResults").length-1);break;case 38:s--;s=Math.max(s,0);break}this.set("currentIndex",s)},setCurrentIndex:function(e){this.set("currentIndex",e)},focusOut:function(e){if(!this.get("mouseOver")){this.set("currentIndex",0);this.set("searchResults",Ember.A())}},changeMouseState:function(e){this.set("mouseOver",e)}},setValidValue:function(e){var t=false;var s=this.get("searchText");var i=this;if(!Ember.isEmpty(e)){$.each(e,function(e,r){if(r.get(i.get("primaryText"))==s){t=true}})}this.set("isValid",t);if(!t&&Ember.isEmpty(s)&&s.length>0){this.set("cssclass","input-error")}else{this.set("cssclass","")}},validateSearchText:function(){this.setValidValue(this.get("searchResults"))}});Ember.Application.initializer({name:"auto-complete-component",initialize:function(t,s){t.register("component:auto-complete",e)}})})();