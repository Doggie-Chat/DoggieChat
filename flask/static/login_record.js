// Function to get an element by ID, with support for passing the element itself
var $$ = function(id) {
	return "string" == typeof id ? document.getElementById(id) : id;
};

// Object for creating new classes
var Class = {
	create: function() {
		return function() {
			this.initialize.apply(this, arguments);
		}
	}
}

// Function for extending objects
Object.extend = function(destination, source) {
	for(var property in source) {
		destination[property] = source[property];
	}
	return destination;
}

// Calendar class
var Calendar = Class.create();
Calendar.prototype = {
	initialize: function(container, options) {
		this.Container = $$(container); 
		this.Days = []; 
		this.SetOptions(options);
		this.Year = this.options.Year;
		this.Month = this.options.Month;
		this.onToday = this.options.onToday;
		this.onSignIn = this.options.onSignIn;
		this.onFinish = this.options.onFinish;
		this.qdDay = this.options.qdDay;
		this.isSignIn = false;
		this.Draw();
	},
	// Set default options
	SetOptions: function(options) {
		this.options = { 
			Year: new Date().getFullYear(), // Year to display
			Month: new Date().getMonth() + 1, // Month to display
			qdDay: null,
			onToday: function() {}, 
			onSignIn: function(){}, 
			onFinish: function() {} 
		};
		Object.extend(this.options, options || {});
	},
	/// Previous month
	PreMonth: function() {
		// Get the date object for the previous month
		var d = new Date(this.Year, this.Month - 2, 1);
		// Update properties
		this.Year = d.getFullYear();
		this.Month = d.getMonth() + 1;
		// Redraw the calendar
		this.Draw();
	},
	// Next month
	NextMonth: function() {
		var d = new Date(this.Year, this.Month, 1);
		this.Year = d.getFullYear();
		this.Month = d.getMonth() + 1;
		this.Draw();
	},
	// Draw the calendar
	Draw: function() {
		// Checked in dates
		var day = this.qdDay;
		// Date list
		var arr = [];
		// Get the number of days from the previous month that appear in the first week of this month
		for(var i = 1, firstDay = new Date(this.Year, this.Month - 1, 1).getDay(); i <= firstDay; i++) {
			arr.push("&nbsp;");
		}
		// Get the number of days in this month
		for(var i = 1, monthDay = new Date(this.Year, this.Month, 0).getDate(); i <= monthDay; i++) {
			arr.push(i);
		}
		var frag = document.createDocumentFragment();
		this.Days = [];
		while(arr.length > 0) {
			// Insert a "tr" every week
			var row = document.createElement("tr");
			// 7 days in a week
			for(var i = 1; i <= 7; i++) {
				var cell = document.createElement("td");
				cell.innerHTML = "&nbsp;";
				if(arr.length > 0) {
					var d = arr.shift();
					cell.innerHTML = "<span>" + d + "</span>";
					if(d > 0 && day.length) {
						for(var ii = 0; ii < day.length; ii++) {
							this.Days[d] = cell;
							// Successfully checked in
							if(this.IsSame(new Date(this.Year, this.Month - 1, d), day[ii])) {
								this.onToday(cell);
							}
							// whether to check in today
							if(this.checkSignIn(new Date(), day[ii])) {
								this.onSignIn();
							}
						}
					}
				}
				row.appendChild(cell);
			}
			frag.appendChild(row);
		}
		// Clear content before inserting
		while(this.Container.hasChildNodes()) {
			this.Container.removeChild(this.Container.firstChild);
		}
		this.Container.appendChild(frag);
		this.onFinish();
		if(this.isSignIn) {
			this.isSignIn = false;
			return this.SignIn();
		}
	},
	// Whether to check in or not
	IsSame: function(d1, d2) {
		d2 = new Date(d2 * 1000);
		return(d1.getFullYear() == d2.getFullYear() && d1.getMonth() == d2.getMonth() && d1.getDate() == d2.getDate());
	},
	// Whether to check in today
	checkSignIn: function(d1, d2) {
		d2 = new Date(d2 * 1000);
		return(d1.getFullYear() == d2.getFullYear() && d1.getMonth() == d2.getMonth() && d1.getDate() == d2.getDate());
	},
	// Check in 
	SignIn: function() {
		var now = new Date();
		var Year = now.getFullYear();
		var Month = now.getMonth() + 1;
		if(Year != this.Year || Month != this.Month) {
			this.Year = Year;
			this.Month = Month;
			this.isSignIn = true;
			return this.Draw();
		}
		var day = now.getDate();
		var arr = new Array();
		var tb = document.getElementById('idCalendar');
		for(var i = 0; i < tb.rows.length; i++) {
			for(var j = 0; j < tb.rows[i].cells.length; j++) {
				if(day == tb.rows[i].cells[j].innerText && Year == this.Year && Month == this.Month) {
					if(tb.rows[i].cells[j].className == "onToday"){
						return 2;
					}
					tb.rows[i].cells[j].className = "onToday"
					this.qdDay.push(Date.parse(new Date()) / 1000)
					return 1;
					
				}
			}
		}
	}
};




// Calendar with check-in feature and event handling
var isSign = false;
var myday = new Array(); //Checked-in array

var cale = new Calendar("idCalendar", {
	qdDay: myday,
	onToday: function(o) {
		o.className = "onToday";
	},
	onSignIn: function (){
		$$("sign-txt").innerHTML = 'Success';
	},
	onFinish: function() {
		$$("sign-count").innerHTML = myday.length // Number of check-ins
		$$("idCalendarYear").innerHTML = this.Year;
		$$("idCalendarMonth").innerHTML = this.Month; // header year and month

	}
});
$$("idCalendarPre").onclick = function() {
	cale.PreMonth();
}
$$("idCalendarNext").onclick = function() {
	cale.NextMonth();
}
// Add today's check-in
$$("signIn").onclick = function() {
	if(isSign == false) {
		var res = cale.SignIn();
		if(res == '1') {
			$$("sign-txt").innerHTML = 'Success';
			$$("sign-count").innerHTML = parseInt($$("sign-count").innerHTML) + 1;
			isSign = true;
		} else if (res == '2'){
			$$("sign-txt").innerHTML = 'Success';
			alert('Already Checked In Today')
		}
	} else {
		alert('Already Checked In Today')
	}
}

