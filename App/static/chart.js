let modal;

function viewEvaluation(evaluationId){
    modal =  document.querySelector('#evaluation_modal');

    modal = M.Modal.init(
    modal,
        {
            onOpenEnd: ()=>renderData(evaluationId),
        }
    );

    modal.open();
}


function closeEvaluation(){
    modal.close();
  
}

async function renderData(evaluationId){
    let response = await fetch(`/get-evaluation/${evaluationId}`);
    let { series, name, score, comments } = await response.json();

    let commens = document.querySelector('#comments');
    commens.innerHTML = `
    <div class="row">
        <div class="input-field col s12">
        <textarea name="notes" class="materialize-textarea" placeholder="comments" disabled>${comments}</textarea>
        <label for="notes" class="active" style="font-size: large;">Reviewer's Comments</label>
        </div>
    </div>`;


    Highcharts.chart('container', {

        chart: {
            polar: true,
            type: 'line'
        },
    
        title: {
            text: `Evaluation of ${name}`,
            x: -80
        },
    
        pane: {
            size: '80%'
        },
    
        xAxis: {
            categories: 
            [
                'Novelty',
                'Relevance', 
                'Feasibility', 
                'Impact',
                'Sustainability', 
                'Technology'
            ],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },
    
        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
        },
    
        tooltip: {
            shared: true,
            pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y:,.0f}</b><br/>'
        },
    
        legend: {
            align: 'right',
            verticalAlign: 'middle',
            layout: 'vertical'
        },
    
        series,
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom',
                        layout: 'horizontal'
                    },
                    pane: {
                        size: '70%'
                    }
                }
            }]
        }
    
    });

    let res = document.querySelector('#res');
    res.innerHTML = `
        <p class="card-title">Overall Score ${score}</p>
    `; 
}


html = `<div class="row" >


`;