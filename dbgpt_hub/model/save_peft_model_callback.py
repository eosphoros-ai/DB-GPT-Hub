import os
from typing import Any, Dict

import transformers
from transformers.trainer_utils import PREFIX_CHECKPOINT_DIR


class SavePeftModelCallback(transformers.TrainerCallback):
    """
    A TrainerCallback that saves the PEFT model checkpoint during training.
    """

    def save_model(
        self, args: Any, state: transformers.TrainingArguments, kwargs: Dict[str, Any]
    ) -> None:
        """
        Saves the PEFT model checkpoint.

        Args:
            args (Any): The command line arguments passed to the script.
            state (transformers.TrainingArguments): The current state of training.
            kwargs (Dict[str, Any]): A dictionary of additional keyword arguments.

        Raises:
            TypeError: If `state` is not an instance of `transformers.TrainingArguments`.
        """
        print("Saving PEFT checkpoint...")

        if state.best_model_checkpoint is not None:
            # If best model checkpoint exists, use its directory as the checkpoint folder
            checkpoint_folder = os.path.join(
                state.best_model_checkpoint, "adapter_model"
            )
        else:
            # Otherwise, create a new checkpoint folder using the output directory and current global step
            checkpoint_folder = os.path.join(
                args.output_dir, f"{PREFIX_CHECKPOINT_DIR}-{state.global_step}"
            )

        # Create path for the PEFT model
        peft_model_path = os.path.join(checkpoint_folder, "adapter_model")
        kwargs["model"].save_pretrained(peft_model_path)

        # Create path for the PyTorch model binary file and remove it if it already exists
        pytorch_model_path = os.path.join(checkpoint_folder, "pytorch_model.bin")
        if os.path.exists(pytorch_model_path):
            os.remove(pytorch_model_path)

    def on_save(
        self,
        args: Any,
        state: transformers.TrainingArguments,
        control: transformers.trainer_callback.TrainerControl,
        **kwargs: Dict[str, Any],
    ) -> transformers.trainer_callback.TrainerControl:
        """
        Callback method that calls save_model() and returns `control` argument.

        Args:
            args (Any): The command line arguments passed to the script.
            state (transformers.TrainingArguments): The current state of training.
            control (transformers.trainer_callback.TrainerControl): \
                The current state of the TrainerCallback's control flow.
            kwargs (Dict[str, Any]): A dictionary of additional keyword arguments.

        Returns:
            transformers.trainer_callback.TrainerControl: The current state of the TrainerCallback's control flow.

        Raises:
            TypeError: If `state` is not an instance of `transformers.TrainingArguments`.
        """
        self.save_model(args, state, kwargs)
        return control

    def on_train_end(
        self,
        args: Any,
        state: transformers.TrainingArguments,
        control: transformers.trainer_callback.TrainerControl,
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Callback method that saves the model checkpoint and creates a 'completed' file in the output directory.

        Args:
            args (Any): The command line arguments passed to the script.
            state (transformers.TrainingArguments): The current state of training.
            control (transformers.trainer_callback.TrainerControl): \
                The current state of the TrainerCallback's control flow.
            kwargs (Dict[str, Any]): A dictionary of additional keyword arguments.

        Raises:
            TypeError: If `state` is not an instance of `transformers.TrainingArguments`.
        """

        # Define a helper function to create a 'completed' file in the output directory
        def touch(fname, times=None):
            with open(fname, "a"):
                os.utime(fname, times)

        # Create the 'completed' file in the output directory
        touch(os.path.join(args.output_dir, "completed"))

        # Save the model checkpoint
        self.save_model(args, state, kwargs)
