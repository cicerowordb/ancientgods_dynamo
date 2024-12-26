""" Contains localized debug, info, warning, and error messages for the application.
    Messages are organized by category (`DEBUG`, `INFO`, `WARNING`, `ERROR`) and support
    multiple languages (`pt-br`, `en-us`). These messages provide feedback for various
    operations such as loading data, handling requests, and managing `AncientGod` entities.
"""

DEBUG = {
    'pt-br': {
        'start_loading_data': 'Iniciando carregamento dos dados para o DynamoDB',
        'add_request_received': 'Recebida solicitação para adicionar um novo AncientGod',
        'list_request_received': 'Recebida solicitação para listar todos os AncientGods',
        'delete_request_received': 'Recebida solicitação para remover AncientGod: {name}',
        'read_request_received': 'Recebida solicitação para buscar AncientGod: {name}',
        'app_start': 'Iniciando aplicação Flask.'
    },
    'en-us': {
        'start_loading_data': 'Start loading data to DynamoDB',
        'add_request_received': 'Request received to add a new AncientGod',
        'list_request_received': 'Request received to list all AncientGods',
        'delete_request_received': 'Request received to delete AncientGod: {name}',
        'read_request_received': 'Request received to fetch AncientGod: {name}',
        'app_start': 'Starting Flask application.'
    }
}

INFO = {
    'pt-br': {
        'item_inserted': 'Item inserido: {name}',
        'god_added': "AncientGod '{name}' adicionado com sucesso.",
        'god_removed': "AncientGod '{name}' removido com sucesso.",
        'list_items_count': '{count} itens recuperados do DynamoDB.',
        'json_data_loaded': 'Dados carregados do arquivo JSON com sucesso.',
        'god_fetched': "AncientGod '{name}' recuperado com sucesso."
    },
    'en-us': {
        'item_inserted': 'Item inserted: {name}',
        'god_added': "AncientGod '{name}' added successfully.",
        'god_removed': "AncientGod '{name}' removed successfully.",
        'list_items_count': '{count} items retrieved from DynamoDB.',
        'json_data_loaded': 'Data successfully loaded from JSON file.',
        'god_fetched': "AncientGod '{name}' fetched successfully."
    }
}

WARNING = {
    'pt-br': {
        'missing_required_fields': 'Campos obrigatórios ausentes na solicitação',
        'god_not_found': "AncientGod '{name}' não encontrado."
    },
    'en-us': {
        'missing_required_fields': 'Required fields missing in the request',
        'god_not_found': "AncientGod '{name}' not found."
    }
}

ERROR = {
    'pt-br': {
        'add_god_error': 'Erro ao adicionar AncientGod: {err}',
        'list_gods_error': 'Erro ao listar AncientGods: {err}',
        'delete_god_error': 'Erro ao remover AncientGod: {err}',
        'json_load_error': 'Erro ao carregar dados do arquivo JSON: {err}',
        'read_god_error': 'Erro ao buscar AncientGod: {err}'
    },
    'en-us': {
        'add_god_error': 'Error adding AncientGod: {err}',
        'list_gods_error': 'Error listing AncientGods: {err}',
        'delete_god_error': 'Error deleting AncientGod: {err}',
        'json_load_error': 'Error loading data from JSON file: {err}',
        'read_god_error': 'Error fetching AncientGod: {err}'
    }
}
