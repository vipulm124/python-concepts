# Import required Python modules
import logging  # For logging functionality
from functools import wraps  # For preserving function metadata in decorators
import contextlib  # For creating context managers

# Define the default logging format - just the message without any additional formatting
DEFAULT_FORMAT = '%(message)s'

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO to capture all levels INFO and above
    format=DEFAULT_FORMAT  # Use our default format for log messages
)

@contextlib.contextmanager  # Define this function as a context manager
def prefix_logger(prefix):
    """Temporarily add a prefix to all logging messages."""
    # Get the root logger instance
    logger = logging.getLogger()
    # Make a copy of current handlers to restore later
    original_handlers = logger.handlers.copy()
    
    # Create a new handler for our prefixed logging
    new_handler = logging.StreamHandler()  # StreamHandler outputs to console
    # Set up the new format with our prefix
    new_handler.setFormatter(logging.Formatter(f'[{prefix}] {DEFAULT_FORMAT}'))
    
    # Remove all existing handlers to prevent duplicate logging
    logger.handlers.clear()
    # Add our new prefixed handler
    logger.addHandler(new_handler)
    
    try:
        # Let the wrapped code execute
        yield
    finally:
        # Cleanup: Remove our temporary handler
        logger.handlers.clear()
        # Restore the original handlers
        for handler in original_handlers:
            logger.addHandler(handler)

def with_logging_prefix(prefix):
    """Decorator factory that takes a prefix parameter."""
    def decorator(func):
        """The actual decorator that wraps the function."""
        @wraps(func)  # Preserve the metadata of the original function
        def wrapper(*args, **kwargs):
            """Wrapper function that adds the logging prefix context."""
            # Use our context manager to temporarily add prefix to logs
            with prefix_logger(prefix):
                # Execute the original function
                return func(*args, **kwargs)
        return wrapper
    return decorator

@with_logging_prefix("abc")  # Apply our decorator with prefix "abc"
def testing_flow():
    """Main test function demonstrating prefixed logging."""
    logging.info("This is an info message before loop")
    internal_loop_function(10)  # Call internal function with 10 iterations
    logging.info("This is an info message after loop")


def internal_loop_function(n):
    """Helper function that logs messages in a loop."""
    for i in range(n):
        logging.info(f"This is an info message in internal loop {i}")


@with_logging_prefix("def")  
def another_function():
    """Second test function with different prefix."""
    logging.info("This is an info message in another function")
    internal_loop_function(5) 


# Execute our test functions
testing_flow()  # Will log with prefix [abc]
another_function()  # Will log with prefix [def]