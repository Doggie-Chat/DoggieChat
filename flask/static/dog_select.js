// This dog_select.js file is used to handle the dog selection
const tabsParentContainer = document.querySelector(".dog-tab-parent");
const tabsMarker = tabsParentContainer.querySelector(".tab_marker");
const visibleTab = tabsParentContainer.querySelector(
   ".tab input:checked + label"
);


// listen user clicks on tabs
tabsParentContainer.addEventListener("change", (e) => {
   let input = e.target;
   
   // toggle visible content
   let existingVisibleContent = tabsParentContainer.querySelector(
      ".tab_content.visible"
   );
   existingVisibleContent.classList.remove("visible");
   let associatedTabContent = tabsParentContainer.querySelector(
      `.tab_content[data-associated-tab="${input.id}"]`
   );
   associatedTabContent.classList.add("visible");

});