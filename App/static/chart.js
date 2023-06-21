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
    document.querySelector('#passSummary').innerHTML = ''
    document.querySelector('#failSummary').innerHTML = ''
    modal.close();
}

async function renderData(evaluationId){
    let response = await fetch(`/get-evaluation/${evaluationId}`);
    let { series, name, score, comments, novelty, relevance, feasibility, impact, sustainability, technologies} = await response.json();

    let commens = document.querySelector('#comments');
    commens.innerHTML = `
    <div class="row">
        <div class="input-field col s12">
        <p name="notes" style="font-size:large;" class="materialize-textarea" disabled>${comments}</p>
        <label for="notes" class="active" style="font-size:large;">Reviewer's Comments</label>
        </div>
    </div>`;

    document.querySelector('#res').innerHTML = `
        <p class="card-title">Overall Score ${score}</p>
    `; 

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

    let grades = [novelty, relevance, feasibility, technologies, impact, sustainability];
    for (i in grades) {
        if(grades[i].score < grades[i].threshold){
        document.querySelector('#failSummary').innerHTML += `
            <p style="font-size:large;">${grades[i].name} failed: Score is ${grades[i].score}; threshold is ${grades[i].threshold}</p>
         `;
        }else{
            document.querySelector('#passSummary').innerHTML += `
                <p style="font-size:large;">${grades[i].name} passed: Score is ${grades[i].score}; threshold is ${grades[i].threshold}</p>
            `;
        }
    }

html = `<div class="row" >
`;
}