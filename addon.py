from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():

    classes = [
        {
            'label': 'Neural Networks for Machine Learning',
            'path': plugin.url_for("showClass", className="neuralnetworks")
        }, {
            'label': 'Data Structures',
            'path': plugin.url_for("showClass", className="datastructures")
        }, {
            'label': 'Robotics: Aerial Robotics',
            'path': plugin.url_for("showClass", className="aerialrobotics")
        }
    ]

    return classes

@plugin.route('/class/<className>')
def showClass(className):
        lectures = [
            {
                'label': className + " " + 'Week I',
                'path': 'http://s3.amazonaws.com/KA-youtube-converted/JwO_25S_eWE.mp4/JwO_25S_eWE.mp4',
                'is_playable': True
            }, {
                'label': className + " " + 'Week II',
                'path': 'http://s3.amazonaws.com/KA-youtube-converted/JwO_25S_eWE.mp4/JwO_25S_eWE.mp4',
                'is_playable': True
            }, {
                'label': className + " " + 'Week III',
                'path': 'http://s3.amazonaws.com/KA-youtube-converted/JwO_25S_eWE.mp4/JwO_25S_eWE.mp4',
                'is_playable': True
            },
        ]

        return lectures

if __name__ == '__main__':
    plugin.run()
