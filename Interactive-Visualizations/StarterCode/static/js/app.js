// Construct URL
const url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";

function buildDataset(sample) 
{
	d3.json(url).then((data) => 
    {
		let metadata = data.metadata;

		// Filter the data to find the object that matches the specified sample number
		let result_array = metadata.filter(sampleObj => sampleObj.id == sample);
		let result = result_array[0];
		
		// Use d3 to select the panel with id of `#sample-metadata`, clear existing metadata
		d3.select("#sample-metadata").html("");
		
		// Append new HTML tags for each key-value pair in the metadata
		 for (key in result)
        {
            d3.select("#sample-metadata").append("h5").text(`${key}: ${result[key]}`);
		};	
	});
};

// create a function to build the charts
function buildCharts(sample) {
	d3.json(url).then((data) => 
    {
		let samples = data.samples;
		let result_array = samples.filter(sampleObj => sampleObj.id == sample);
		let result = result_array[0];
		let otu_ids = result.otu_ids;
		let otu_labels = result.otu_labels;
		let sample_values = result.sample_values;
	
    let colorscale = [
        [0, '#F2671F'],
        [0.25, '#C91B26'],
        [0.5, '#9C0F5F'],
        [0.75, '#60047A'],
        [1, '#160A47']];

	// bubble chart
    let bubble_chart = 
    {
        text: otu_labels,
        y: sample_values,
        x: otu_ids,
        mode: "markers",
        marker: {
          size: sample_values,
          color: otu_ids,
          colorscale:  colorscale}
    };

  // bubble chart layout
  var bubble_layout = 
    {
      title: {text: "Bacteria Cultures Per Sample", font: {size: 20}},
      hovermode: "closest",
      xaxis: {title: "OTU ID"},
      yaxis: {title: "Culture Total"},
      font: { color: "black", family: "Arial"},
      width: 600, 
      height: 400 
    };

  // Bubble Chart to Plotly
  Plotly.newPlot("bubble", [bubble_chart], bubble_layout);
		
  // Build a Bar Chart
  let bar_y = otu_ids.slice(0,10).map(id => `OTU ${id}`).reverse()
  let bar_x = sample_values.slice(0,10).reverse()
  let bar_labels = otu_labels.slice(0,10).reverse()

  // bar chart layout
  let bar_chart = 
    {
    y: bar_y,
    x: bar_x,
    text: bar_labels,
    type: "bar",
    orientation: "h",
    marker: {color: "#7F0B4D"}   
    };

  // Layout set up
  var bar_layout = 
    {
    title: {text: "Top Belly Button Bacteria", font: {size: 20}},
    font: { color: "black", family: "Arial"},
    width: 600, 
    height: 400 
    };

  // Render the plot to the div tag with id "bar"
  Plotly.newPlot("bar", [bar_chart], bar_layout)
  })
};

// Build a gauge chart
function buildGaugeChart(sample) 
{
  d3.json(url).then((data) => 
  {
    let metadata = data.metadata;

    // Filter the data with the desired sample number
    let result_array = metadata.filter(sampleObj => sampleObj.id == sample);
    let result = result_array[0];

    // Create variable and turn into float 
    var frequency = parseFloat(result.wfreq);

    var gauge_data = [
      {
        domain: {x: [0, 1], y: [0, 1]},
        value: frequency,
        title: {text: "Belly Button Washing Frequency", font: {size: 20}},
        type: "indicator",
        mode: "gauge+number",
        gauge: {
          axis: { range: [null, 10]},
          bar: {color: "blue"},
          steps: [
            { range: [0, 1], color: "#F2671F"},
            { range: [1, 2], color: "#ED6E35"},
            { range: [2, 3], color: "#D95C2F"},
            { range: [3, 4], color: "#C91B26"},
            { range: [4, 5], color: "#B31A24"},
            { range: [5, 6], color: "#9C0F5F"},
            { range: [6, 7], color: "#7F0B4D"},
            { range: [7, 8], color: "#60047A"},
            { range: [8, 9], color: "#3B0A4A"},
            { range: [9, 10], color: "#160A47"}],
        //   number: {font: {size: 10}}
        // Next steps: determine how to change gauge font size
        }
      }
    ];

    // Create the layout for the gauge chart.
    var gauge_layout = {
      width: 500,
      height: 300,
      margin: { t: 25, r: 25, l: 25, b: 25},
      font: { color: "black", family: "Arial"}
    };

    // Use Plotly to plot the gauge data and layout.
    Plotly.newPlot("gauge", gauge_data, gauge_layout);
  });
};

// Function to run the dashboard 
function run() 
{
  // Grab a datapoint to the dropdown 
  let selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json(url).then((data) => 
  {
    let sample_names = data.names;

	// Loop for append
    for (let i = 0; i <sample_names.length; i++)
    {
      // Append to the selector object
      selector
        .append("option")
        .text(sample_names[i])
        .property("value", sample_names[i]);
    };

    // Use the first sample from the list to build the initial plots
    let first_sample = sample_names[0];
    buildCharts(first_sample);
    buildDataset(first_sample);
    buildGaugeChart(first_sample);
  });
};

// use optionChanged() function in html
function optionChanged(sample_fetch) 
{
  // fetch everytime a new sample is selected
  buildCharts(sample_fetch);
  buildDataset(sample_fetch);
  buildGaugeChart(sample_fetch);
};

// run dashboard
run();