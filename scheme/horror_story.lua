box.cfg{
    listen=3301
}

box.schema.user.grant('guest', 'read,write,execute', 'universe', nil, {if_not_exists=true})

box.once("horror_story", function()
    box.schema.sequence.create('story_S')
    box.schema.space.create('story', {
        if_not_exists = true,
        format={
             {name = 'id', type = 'unsigned'},
             {name = 'story', type = 'string'}
        }
    })
    box.space.story:create_index('id', {
        sequence = 'story_S',
        parts = {'id'}
    })    
    box.schema.space.create('user', {
        if_not_exists = true,
        format={
            {name = 'id', type = 'string'},
            {name = 'update', type = 'boolean'},
            {name = 'count_story', type = 'unsigned'},
            {name = 'id_story', type = 'array'},
            {name = 'line', type = 'unsigned'}
        }
    })
    box.space.user:create_index('id', {
        type = 'hash',
        parts = {'id'},
        if_not_exists = true,
        unique = true
    })    
end
)