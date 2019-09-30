Object
  .getOwnPropertyNames(data)
  .forEach((i, j) => {
    var annotations = [],
      traces = [];

    let obj = data[i];

    Object
      .getOwnPropertyNames(obj)
      .forEach((val, ind, arr) => {
        traces.push({ y: obj[val], name: val, type: 'box' });
        annotations.push({
          x: ind + .35,
          y: obj[val][2],
          text: obj[val][2].toFixed(2),
          showarrow: false,
          align: 'center'
        });
      });
    var layout = {
      title: "Benchmark for " + i,
      yaxis: {
        min: 0,
        title: 'Elapsed time [ms]',
        zeroline: true
      },
      annotations: annotations,
      showlegend: false
    };

    let tag = 'fig_' + i
      .toLocaleLowerCase()
      .replace(/ /g, '_');

    Plotly.plot(document.getElementById(tag), traces, layout);
  });
