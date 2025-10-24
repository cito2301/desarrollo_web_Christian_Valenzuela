async function fetchJson(url) {
  const r = await fetch(url);
  return r.ok ? r.json() : null;
}

document.addEventListener("DOMContentLoaded", async () => {
  const dia = await fetchJson('/api/estadisticas/avisos-por-dia');
  if (dia) {
    const categories = dia.map(d => d[0]);
    const data = dia.map(d => d[1]);
    Highcharts.chart('chart-dia', {
      chart: { type: 'line' },
      title: { text: 'Avisos de adopción por día' },
      xAxis: { categories: categories, title: { text: 'Día' } },
      yAxis: { title: { text: 'Cantidad de avisos' } },
      series: [{ name: 'Avisos', data: data }]
    });
  }

  const tipo = await fetchJson('/api/estadisticas/avisos-por-tipo');
  if (tipo) {
    const series = Object.keys(tipo).map(k => ({ name: k, y: tipo[k] }));
    Highcharts.chart('chart-tipo', {
      chart: { type: 'pie' },
      title: { text: 'Distribución de avisos por tipo de mascota' },
      tooltip: { pointFormat: '{series.name}: <b>{point.y}</b>' },
      series: [{ name: 'Total', data: series }]
    });
  }

  const mes = await fetchJson('/api/estadisticas/avisos-por-mes-tipo');
  if (mes) {
    const monthNames = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"];
    const months = [...new Set(mes.map(m => m.mes))].sort((a, b) => a - b);

    const gatos = months.map(m => {
      const r = mes.find(x => x.mes === m && x.tipo === 'gato');
      return r ? r.cnt : 0;
    });

    const perros = months.map(m => {
      const r = mes.find(x => x.mes === m && x.tipo === 'perro');
      return r ? r.cnt : 0;
    });

    Highcharts.chart('chart-mes', {
      chart: { type: 'column' },
      title: { text: 'Avisos por mes y tipo de mascota' },
      xAxis: {
        categories: months.map(m => monthNames[m - 1] || m),
        title: { text: 'Mes' }
      },
      yAxis: {
        min: 0,
        title: { text: 'Cantidad de avisos' }
      },
      tooltip: {
        shared: true,
        valueSuffix: ' avisos'
      },
      series: [
        { name: 'Gatos', data: gatos },
        { name: 'Perros', data: perros }
      ]
    });
  }
});
