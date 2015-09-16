(function ($)

            $('#diva-wrapper').diva({
            enableAutoHeight: true,
            fixedHeightGrid: false,
            enableAutoTitle: false,
            iipServerURL: "{{ IIP_SERVER }}",
            objectData: "{{ DIVA_OBJECT_DATA }}" + "{{ content.id }}.json",
            imageDir: "{{ IIP_SERVER_IMAGE_PATH }}" + "{{ content.id }}",
            enableCanvas: false,
            enableDownload: false,
            blockMobileMove: false,
            enableZoomControls: 'buttons',
            inBookLayout: false,
            zoomLevel: 2,
            enableHighlight: false
        });

        $('.tune-page-link').click(function(e)
        {
            var diva = $('#diva-wrapper').data('diva');
            var pageNum = $(this).data('page');
            diva.gotoPageByNumber(pageNum);
            e.preventDefault();
                regions = [{
                    'width': $(this).data('w'),
                    'height': $(this).data('h'),
                    'ulx': $(this).data('x'),
                    'uly': $(this).data('y'),
                }];
            diva.highlightOnPage(pageNum-1, regions);
        });